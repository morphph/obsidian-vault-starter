# Claude Code Official Docs — Push events into a running session with channels

Captured 2026-05-14 from https://code.claude.com/docs/en/channels.md

> Use channels to push messages, alerts, and webhooks into your Claude Code session from an MCP server. Forward CI results, chat messages, and monitoring events so Claude can react while you're away.

> [!note]
> Channels are in research preview and require Claude Code v2.1.80 or later. They require Anthropic authentication through claude.ai or a Console API key, and are not available on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry. Team and Enterprise organizations must explicitly enable them.

A channel is an MCP server that pushes events into your running Claude Code session, so Claude can react to things that happen while you're not at the terminal. Channels can be two-way: Claude reads the event and replies back through the same channel, like a chat bridge. Events only arrive while the session is open, so for an always-on setup you run Claude in a background process or persistent terminal.

Unlike integrations that spawn a fresh cloud session or wait to be polled, the event arrives in the session you already have open.

You install a channel as a plugin and configure it with your own credentials. Telegram, Discord, and iMessage are included in the research preview.

When Claude replies through a channel, you see the inbound message in your terminal but not the reply text. The terminal shows the tool call and a confirmation (like "sent"), and the actual reply appears on the other platform.

## Supported channels

Each supported channel is a plugin that requires Bun.

### Telegram

1. Create a Telegram bot via @BotFather, get token
2. `/plugin install telegram@claude-plugins-official`
3. `/reload-plugins`
4. `/telegram:configure <token>` (saves to `~/.claude/channels/telegram/.env`)
5. Exit Claude, restart with: `claude --channels plugin:telegram@claude-plugins-official`
6. DM your bot → bot replies with pairing code
7. `/telegram:access pair <code>` → `/telegram:access policy allowlist`

### Discord

1. Discord Developer Portal → New Application, enable Message Content Intent
2. OAuth2 URL Generator → bot scope + permissions (View Channels, Send Messages, etc.)
3. `/plugin install discord@claude-plugins-official` → `/reload-plugins`
4. `/discord:configure <token>`
5. `claude --channels plugin:discord@claude-plugins-official`
6. DM bot → pair: `/discord:access pair <code>` → `/discord:access policy allowlist`

### iMessage (macOS only)

1. Grant Full Disk Access (for `~/Library/Messages/chat.db`)
2. `/plugin install imessage@claude-plugins-official`
3. `claude --channels plugin:imessage@claude-plugins-official`
4. Text yourself (bypasses access control)
5. Allow other senders: `/imessage:access allow +15551234567`

## Quickstart with fakechat

Fakechat = officially supported demo channel running chat UI on localhost.

```text
/plugin install fakechat@claude-plugins-official
```

Exit and restart:

```bash
claude --channels plugin:fakechat@claude-plugins-official
```

Open http://localhost:8787 → message arrives as `<channel source="fakechat">` event.

If Claude hits a permission prompt while you're away, the session pauses. Channel servers that declare the permission relay capability can forward these prompts. For unattended use, `--dangerously-skip-permissions` bypasses prompts entirely.

When running channels in non-interactive mode with `-p`, tools that need terminal input (multiple-choice questions, plan mode approval) are disabled.

## Security

Every approved channel plugin maintains a sender allowlist: only IDs you've added can push messages, everyone else silently dropped.

Telegram/Discord bootstrap via pairing. iMessage detects own addresses from Messages database at startup.

On top of that, you control which servers are enabled each session with `--channels`, and your organization controls availability with `channelsEnabled` on Team/Enterprise plans.

Being in `.mcp.json` isn't enough to push messages: a server also has to be named in `--channels`.

The allowlist also gates permission relay if the channel declares it. Anyone who can reply through the channel can approve or deny tool use in your session.

## Enterprise controls

Two managed settings users cannot override:

| Setting | Purpose | When not configured |
| :--- | :--- | :--- |
| `channelsEnabled` | Master switch. Must be `true`. | claude.ai Team/Enterprise: blocked. Console: allowed unless managed settings deploy. |
| `allowedChannelPlugins` | Which plugins can register. Replaces Anthropic list when set. | Anthropic default list applies |

Pro and Max users without an organization skip these checks entirely.

Enable from claude.ai Admin settings → Claude Code → Channels.

```json
{
  "channelsEnabled": true,
  "allowedChannelPlugins": [
    { "marketplace": "claude-plugins-official", "plugin": "telegram" },
    { "marketplace": "claude-plugins-official", "plugin": "discord" },
    { "marketplace": "acme-corp-plugins", "plugin": "internal-alerts" }
  ]
}
```

## Research preview

Availability rolling out gradually. `--channels` flag syntax may change. Only plugins from Anthropic-maintained allowlist (or org allowlist). For development: `--dangerously-load-development-channels`.

## How channels compare

| Feature | What it does | Good for |
| --- | --- | --- |
| Claude Code on the web | Runs in fresh cloud sandbox, cloned from GitHub | Self-contained async work |
| Claude in Slack | Spawns web session from `@Claude` mention | Tasks from team conversation |
| Standard MCP server | Claude queries it during a task | On-demand access to read/query |
| Remote Control | Drive local session from claude.ai or mobile app | Steering in-progress session |

Channels fill the gap by pushing events from non-Claude sources into already-running local session.

* **Chat bridge**: ask Claude from phone via Telegram/Discord/iMessage
* **Webhook receiver**: CI/error tracker/deploy pipeline → already-open session

## Next steps

* Build your own channel: Channels reference
* Remote Control to drive local session from phone
* Scheduled tasks to poll on timer instead of reacting
