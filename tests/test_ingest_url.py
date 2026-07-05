#!/usr/bin/env python3
"""Offline tests for the ingest-url black-box verb (scripts/ingest_url.py).

No claude / no network / no Max: the agent is replaced by a fake binary via
INGEST_URL_CLAUDE_CMD whose behavior is driven by the FAKE_MODE env var.
Each test runs against a throwaway repo skeleton (raw/ + events/ + the two
real scripts copied in), so REPO_ROOT resolution is exercised for real and
the production vault is never touched.

Run: python3 tests/test_ingest_url.py
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REAL_REPO = Path(__file__).resolve().parent.parent
URL = "https://example.com/some-article"

FAKE_CLAUDE = '''#!/usr/bin/env python3
import json, os, sys
from pathlib import Path

mode = os.environ.get("FAKE_MODE", "success")
raw = Path("raw")
Path("spawned.marker").write_text("yes")

HEADER = "# Fake Article\\n\\n**Source:** https://example.com/some-article\\n**Fetch method:** WebFetch\\n\\n"
BODY = ("lorem ipsum dolor sit amet " * 40) + "\\n"

def out(result):
    print(json.dumps({"subtype": "success", "num_turns": 3,
                      "duration_ms": 1200, "total_cost_usd": 0.01,
                      "result": result}))

if mode == "success":
    p = raw / "2026-07-05-fake-article.md"
    p.write_text(HEADER + BODY)
    out("INGEST_RAW_PATH=raw/2026-07-05-fake-article.md")
elif mode == "fetch_failed":
    out("INGEST_FAILED=both fetch methods returned empty content")
elif mode == "raw_missing":
    out("INGEST_RAW_PATH=raw/2026-07-05-ghost.md")
elif mode == "multiple":
    (raw / "2026-07-05-fake-article.md").write_text(HEADER + BODY)
    (raw / "2026-07-05-stray-note.md").write_text(HEADER + BODY)
    out("INGEST_RAW_PATH=raw/2026-07-05-fake-article.md")
elif mode == "bad_header":
    (raw / "2026-07-05-fake-article.md").write_text(
        "# Fake Article\\n\\n**Source:** https://evil.example.com/other\\n\\n" + BODY)
    out("INGEST_RAW_PATH=raw/2026-07-05-fake-article.md")
elif mode == "too_small":
    (raw / "2026-07-05-fake-article.md").write_text(HEADER[:80])
    out("INGEST_RAW_PATH=raw/2026-07-05-fake-article.md")
sys.exit(0)
'''


class IngestUrlTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="ingest-url-test-"))
        (self.tmp / "raw").mkdir()
        (self.tmp / "events").mkdir()
        (self.tmp / "scripts").mkdir()
        for name in ("obsidian_content.py", "ingest_url.py"):
            shutil.copy(REAL_REPO / "scripts" / name, self.tmp / "scripts" / name)
        fake = self.tmp / "fake_claude.py"
        fake.write_text(FAKE_CLAUDE)
        self.fake_cmd = f"{sys.executable} {fake}"

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_verb(self, mode: str | None = "success", extra: list[str] | None = None,
                 url: str = URL) -> tuple[subprocess.CompletedProcess, dict]:
        env = dict(os.environ)
        env["INGEST_URL_CLAUDE_CMD"] = self.fake_cmd
        if mode is not None:
            env["FAKE_MODE"] = mode
        proc = subprocess.run(
            [sys.executable, str(self.tmp / "scripts" / "ingest_url.py"),
             "--url", url] + (extra or []),
            capture_output=True, text=True, env=env, cwd=self.tmp)
        envelope = json.loads(proc.stdout) if proc.stdout.strip() else {}
        return proc, envelope

    def events_lines(self) -> list[str]:
        f = self.tmp / "events" / "ingest-events.jsonl"
        return f.read_text().splitlines() if f.exists() else []

    def spawned(self) -> bool:
        return (self.tmp / "spawned.marker").exists()

    # ── success path ──────────────────────────────────────────────────────────

    def test_success_envelope_event_and_hash(self):
        proc, env = self.run_verb("success")
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        for key in ("contract_version", "ok", "verb", "artifacts", "warnings", "errors"):
            self.assertIn(key, env)
        self.assertTrue(env["ok"])
        self.assertEqual(env["verb"], "ingest-url")
        a = env["artifacts"]
        self.assertEqual(a["url"], URL)
        self.assertEqual(a["source_path"], "raw/2026-07-05-fake-article.md")
        self.assertEqual(a["title"], "Fake Article")
        self.assertEqual(a["fetch_method"], "WebFetch")
        self.assertTrue(a["recorded"])
        self.assertEqual(a["agent"]["num_turns"], 3)
        # event actually appended + event_id independently recomputable
        lines = self.events_lines()
        self.assertEqual(len(lines), 1)
        event = json.loads(lines[0])
        expect_eid = hashlib.sha1(b"raw/2026-07-05-fake-article.md").hexdigest()[:12]
        self.assertEqual(event["event_id"], expect_eid)
        self.assertEqual(a["event_id"], expect_eid)
        self.assertEqual(event["tier"], 1)
        # content_hash independently recomputable from disk
        blob = (self.tmp / "raw" / "2026-07-05-fake-article.md").read_bytes()
        self.assertEqual(a["content_hash"], hashlib.sha256(blob).hexdigest()[:16])
        self.assertGreaterEqual(a["bytes"], 500)

    def test_idempotent_second_call_does_not_spawn(self):
        self.run_verb("success")
        (self.tmp / "spawned.marker").unlink()
        proc, env = self.run_verb("success")
        self.assertEqual(proc.returncode, 0)
        self.assertTrue(env["ok"])
        self.assertFalse(env["artifacts"]["recorded"])
        self.assertFalse(self.spawned(), "second call must not spawn the agent")
        self.assertEqual(len(self.events_lines()), 1, "no duplicate event")
        expect_eid = hashlib.sha1(b"raw/2026-07-05-fake-article.md").hexdigest()[:12]
        self.assertEqual(env["artifacts"]["event_id"], expect_eid)
        self.assertTrue(any("no-op" in w for w in env["warnings"]))

    def test_backfill_when_raw_exists_without_event(self):
        # simulate an earlier manual capture that never got an event
        (self.tmp / "raw" / "2026-07-05-fake-article.md").write_text(
            "# Fake Article\n\n**Source:** " + URL + "\n**Fetch method:** WebFetch\n\n"
            + "x" * 600)
        proc, env = self.run_verb("success")
        self.assertEqual(proc.returncode, 0)
        self.assertTrue(env["artifacts"]["recorded"])
        self.assertFalse(self.spawned(), "existing capture must not re-spawn")
        self.assertEqual(len(self.events_lines()), 1)
        self.assertTrue(any("backfilled" in w for w in env["warnings"]))

    # ── failure paths (structured errors, exit 1, no event) ──────────────────

    def assert_failure(self, mode: str, token: str):
        proc, env = self.run_verb(mode)
        self.assertEqual(proc.returncode, 1, proc.stdout)
        self.assertFalse(env["ok"])
        self.assertEqual(env["errors"][0], token)
        self.assertEqual(self.events_lines(), [], "failure must not record an event")
        return env

    def test_fetch_failed(self):
        env = self.assert_failure("fetch_failed", "fetch_failed")
        self.assertIn("empty content", env["errors"][1])

    def test_raw_missing(self):
        self.assert_failure("raw_missing", "raw_missing")

    def test_multiple_new_files_are_deleted(self):
        self.assert_failure("multiple", "multiple_new_files")
        self.assertEqual(list((self.tmp / "raw").glob("*.md")), [])

    def test_header_mismatch_deleted(self):
        self.assert_failure("bad_header", "header_mismatch")
        self.assertEqual(list((self.tmp / "raw").glob("*.md")), [])

    def test_content_too_small_deleted(self):
        self.assert_failure("too_small", "content_too_small")
        self.assertEqual(list((self.tmp / "raw").glob("*.md")), [])

    # ── dry-run / usage ───────────────────────────────────────────────────────

    def test_dry_run_never_spawns_or_writes(self):
        proc, env = self.run_verb("success", extra=["--dry-run"])
        self.assertEqual(proc.returncode, 0)
        self.assertTrue(env["ok"])
        self.assertFalse(self.spawned())
        self.assertEqual(list((self.tmp / "raw").glob("*.md")), [])
        self.assertEqual(self.events_lines(), [])

    def test_non_http_url_fails(self):
        proc, env = self.run_verb("success", url="ftp://example.com/x")
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(env["errors"][0], "usage")
        self.assertFalse(self.spawned())


if __name__ == "__main__":
    unittest.main(verbosity=2)
