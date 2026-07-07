#!/usr/bin/env python3
"""Offline tests for the learn black-box verb (scripts/learn_note.py) and the
export-learn verb (scripts/obsidian_content.py).

No claude / no network / no Max: the agent is replaced by a fake binary via
LEARN_CLAUDE_CMD whose behavior is driven by FAKE_MODE. Each test runs against
a throwaway repo skeleton so the production vault is never touched.

Run: python3 tests/test_learn_note.py
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REAL_REPO = Path(__file__).resolve().parent.parent
SOURCE = "raw/2026-07-05-fake-topic.md"
SLUG = "fake-topic"

FAKE_CLAUDE = '''#!/usr/bin/env python3
import json, os, sys
from pathlib import Path

mode = os.environ.get("FAKE_MODE", "success")
slug = "fake-topic"
wiki = Path("wiki"); wiki.mkdir(exist_ok=True)
vdir = Path("visuals") / slug
Path("spawned.marker").write_text("yes")

JINGDU_HEAD = (
    "---\\ntype: source-summary\\ncreated: 2026-07-07\\nlast-updated: 2026-07-07\\n"
    "sources:\\n  - raw/2026-07-05-fake-topic.md\\ntags: []\\n---\\n\\n"
    "# \\u7cbe\\u8bfb\\uff1aFake Topic\\n\\n## \\u7cbe\\u8bfb\\n\\n"
    "**\\u4e00\\u53e5\\u8bdd\\u4e3b\\u65e8**\\uff1athis is the thesis line\\n\\n"
)
BODY = ("\\u6bb5\\u843d\\u5185\\u5bb9 lorem ipsum " * 120) + "\\n"
EMBED = "\\n![[fake-topic-diagram.png]]\\n"

def write_jingdu(embed=True, thesis=True, section=True):
    head = JINGDU_HEAD
    if not thesis:
        head = head.replace("**\\u4e00\\u53e5\\u8bdd\\u4e3b\\u65e8**\\uff1athis is the thesis line\\n\\n", "")
    if not section:
        head = head.replace("## \\u7cbe\\u8bfb\\n\\n", "")
    (wiki / f"source-{slug}.md").write_text(head + BODY + (EMBED if embed else ""))

def write_visual(missing_layer=False):
    (vdir / "layers").mkdir(parents=True, exist_ok=True)
    steps = []
    for i in (1, 2, 3):
        f = f"layers/step-0{i}.svg"
        steps.append({"step": i, "label": f"s{i}", "bbox": [0,0,10,10],
                      "cumulativeBbox": [0,0,10,10], "elementCount": 1, "file": f})
        if not (missing_layer and i == 3):
            (vdir / f).write_text("<svg viewBox=\\"0 0 10 10\\"></svg>")
    (vdir / f"{slug}-diagram.png").write_bytes(b"fakepng")
    (vdir / f"{slug}-diagram.excalidraw").write_text("{}")
    (vdir / "steps.json").write_text(json.dumps(
        {"contract_version": "layer-export.v1", "canvas": {}, "steps": steps}))

def out(result):
    print(json.dumps({"subtype": "success", "num_turns": 5, "duration_ms": 900,
                      "total_cost_usd": 0.02, "result": result}))

if mode == "success":
    write_jingdu(); write_visual()
    out(f"LEARN_DONE=wiki/source-{slug}.md")
elif mode == "no_visual":
    write_jingdu(embed=False)
    out("LEARN_NO_VISUAL=pure narrative essay, nothing to diagram\\nLEARN_DONE=x")
elif mode == "jingdu_missing":
    out(f"LEARN_DONE=wiki/source-{slug}.md")
elif mode == "no_thesis":
    write_jingdu(thesis=False); write_visual()
    out(f"LEARN_DONE=wiki/source-{slug}.md")
elif mode == "visual_incomplete":
    write_jingdu(); write_visual(missing_layer=True)
    out(f"LEARN_DONE=wiki/source-{slug}.md")
elif mode == "agent_failed":
    out("LEARN_FAILED=source file is empty")
sys.exit(0)
'''


def run(repo: Path, argv: list[str], env_extra: dict | None = None) -> tuple[dict, int]:
    env = dict(os.environ)
    env["LEARN_CLAUDE_CMD"] = f"{sys.executable} {repo / 'fake_claude.py'}"
    env.update(env_extra or {})
    proc = subprocess.run([sys.executable, str(repo / "scripts" / "learn_note.py")] + argv,
                          capture_output=True, text=True, cwd=repo, env=env)
    try:
        return json.loads(proc.stdout), proc.returncode
    except json.JSONDecodeError:
        raise AssertionError(f"non-JSON stdout: {proc.stdout!r}\nstderr: {proc.stderr!r}")


def run_oc(repo: Path, argv: list[str]) -> tuple[dict, int]:
    proc = subprocess.run([sys.executable, str(repo / "scripts" / "obsidian_content.py")] + argv,
                          capture_output=True, text=True, cwd=repo)
    return json.loads(proc.stdout), proc.returncode


class LearnNoteTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="learn-test-"))
        for d in ("raw", "wiki", "events", "scripts", "visuals"):
            (self.tmp / d).mkdir()
        (self.tmp / SOURCE).write_text("# Fake Topic\n\n**Source:** https://x.example\n\n" + "body " * 200)
        for s in ("learn_note.py", "obsidian_content.py"):
            shutil.copyfile(REAL_REPO / "scripts" / s, self.tmp / "scripts" / s)
        (self.tmp / "fake_claude.py").write_text(FAKE_CLAUDE)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    # ── learn ──────────────────────────────────────────────────────────────

    def test_happy_path(self):
        env, code = run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "success"})
        self.assertTrue(env["ok"]);  self.assertEqual(code, 0)
        a = env["artifacts"]
        self.assertEqual(a["slug"], SLUG)
        self.assertEqual(a["thesis"], "this is the thesis line")
        self.assertEqual(a["visual"]["steps"], 3)
        self.assertIsNone(a["no_visual_reason"])
        self.assertEqual(env["errors"], [])

    def test_no_visual_accepted(self):
        env, code = run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "no_visual"})
        self.assertTrue(env["ok"]);  self.assertEqual(code, 0)
        self.assertIsNone(env["artifacts"]["visual"])
        self.assertIn("diagram", env["artifacts"]["no_visual_reason"])

    def test_jingdu_missing(self):
        env, code = run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "jingdu_missing"})
        self.assertFalse(env["ok"]);  self.assertEqual(code, 1)
        self.assertEqual(env["errors"][0], "jingdu_missing")

    def test_jingdu_invalid_no_thesis(self):
        env, code = run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "no_thesis"})
        self.assertFalse(env["ok"])
        self.assertEqual(env["errors"][0], "jingdu_invalid")
        # invalid artifacts created by this run are cleaned up
        self.assertFalse((self.tmp / "wiki" / f"source-{SLUG}.md").exists())

    def test_visual_incomplete(self):
        env, code = run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "visual_incomplete"})
        self.assertFalse(env["ok"])
        self.assertEqual(env["errors"][0], "visual_incomplete")
        self.assertFalse((self.tmp / "visuals" / SLUG).exists())

    def test_agent_failed(self):
        env, code = run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "agent_failed"})
        self.assertFalse(env["ok"])
        self.assertEqual(env["errors"][0], "agent_failed")

    def test_source_missing(self):
        env, code = run(self.tmp, ["--source", "raw/2026-01-01-nope.md"])
        self.assertFalse(env["ok"])
        self.assertEqual(env["errors"][0], "source_missing")

    def test_idempotent_noop(self):
        env1, _ = run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "success"})
        self.assertTrue(env1["ok"])
        (self.tmp / "spawned.marker").unlink()
        env2, code = run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "success"})
        self.assertTrue(env2["ok"]);  self.assertEqual(code, 0)
        self.assertFalse((self.tmp / "spawned.marker").exists(), "agent must not re-spawn")
        self.assertIsNone(env2["artifacts"]["agent"])
        self.assertEqual(env1["artifacts"]["jingdu_hash"], env2["artifacts"]["jingdu_hash"])

    def test_force_respawns(self):
        run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "success"})
        (self.tmp / "spawned.marker").unlink()
        env, _ = run(self.tmp, ["--source", SOURCE, "--force"], {"FAKE_MODE": "success"})
        self.assertTrue(env["ok"])
        self.assertTrue((self.tmp / "spawned.marker").exists(), "--force must re-spawn")

    def test_dry_run_never_spawns(self):
        env, code = run(self.tmp, ["--source", SOURCE, "--dry-run"])
        self.assertTrue(env["ok"])
        self.assertFalse((self.tmp / "spawned.marker").exists())

    # ── export-learn ───────────────────────────────────────────────────────

    def test_export_learn_happy(self):
        run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "success"})
        out = self.tmp / "staging"
        env, code = run_oc(self.tmp, ["export-learn", "--slug", SLUG, "--out-dir", str(out)])
        self.assertTrue(env["ok"]);  self.assertEqual(code, 0)
        self.assertTrue((out / "jingdu.md").exists())
        self.assertTrue((out / "diagrams" / "steps.json").exists())
        self.assertTrue((out / "diagrams" / "layers" / "step-01.svg").exists())
        vault = (self.tmp / "wiki" / f"source-{SLUG}.md").read_bytes()
        self.assertEqual((out / "jingdu.md").read_bytes(), vault)
        self.assertEqual(env["artifacts"]["diagrams"]["steps"], 3)

    def test_export_learn_missing_jingdu(self):
        env, code = run_oc(self.tmp, ["export-learn", "--slug", "ghost", "--out-dir",
                                      str(self.tmp / "staging")])
        self.assertFalse(env["ok"]);  self.assertEqual(code, 1)
        self.assertIn("jingdu_missing", env["errors"][0])

    def test_export_learn_no_visual_warns(self):
        run(self.tmp, ["--source", SOURCE], {"FAKE_MODE": "no_visual"})
        out = self.tmp / "staging"
        env, code = run_oc(self.tmp, ["export-learn", "--slug", SLUG, "--out-dir", str(out)])
        self.assertTrue(env["ok"])
        self.assertIsNone(env["artifacts"]["diagrams"])
        self.assertTrue(any("no visual bundle" in w for w in env["warnings"]))
        self.assertTrue((out / "jingdu.md").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
