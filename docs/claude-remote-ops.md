# Claude Code Remote Control Operations

Quick reference for managing Claude Code Remote Control server for the Obsidian project.

## Overview

- **Project Path:** `/home/ubuntu/obsidian-vault-starter`
- **tmux Session:** `obsidian-remote`
- **Log File:** `/home/ubuntu/obsidian-vault-starter/logs/claude-remote.log`

## Commands

### Start Server
```bash
/home/ubuntu/obsidian-vault-starter/scripts/start-claude-remote.sh
```
Creates tmux session and starts Claude Code in remote control mode.
Safe to run multiple times (won't create duplicate sessions).

### Check Status
```bash
/home/ubuntu/obsidian-vault-starter/scripts/check-claude-remote.sh
```
Shows:
- tmux session status
- Claude process status
- Log file info
- Last 30 lines of log

### Restart Server
```bash
/home/ubuntu/obsidian-vault-starter/scripts/restart-claude-remote.sh
```
Stops existing session and starts fresh.

## Via OpenClaw Telegram Bot

If you're using the OpenClaw Telegram bot, you can use:

```
/obsidian-remote status   - Check server status
/obsidian-remote restart  - Restart server
/obsidian-remote start    - Start server (if not running)
```

## Manual tmux Operations

**Attach to session (view live output):**
```bash
tmux attach -t obsidian-remote
```

**Detach from session:** Press `Ctrl+B` then `D`

**Kill session:**
```bash
tmux kill-session -t obsidian-remote
```

**List all sessions:**
```bash
tmux ls
```

## Connection Recovery

If your Claude App connection is lost:

1. **Check if server is running:**
   ```bash
   /home/ubuntu/obsidian-vault-starter/scripts/check-claude-remote.sh
   ```

2. **If not running, restart:**
   ```bash
   /home/ubuntu/obsidian-vault-starter/scripts/restart-claude-remote.sh
   ```

3. **Attach to session to see QR code:**
   ```bash
   tmux attach -t obsidian-remote
   ```

4. **Scan QR code or copy link from log:**
   - Look for connection URL in the terminal
   - Paste in Claude App to reconnect

5. **Via Telegram bot (easiest):**
   ```
   /obsidian-remote restart
   ```
   Then attach to tmux to get new QR code/link

## Logs

**View live logs:**
```bash
tail -f /home/ubuntu/obsidian-vault-starter/logs/claude-remote.log
```

**View last 50 lines:**
```bash
tail -n 50 /home/ubuntu/obsidian-vault-starter/logs/claude-remote.log
```

**Clear old logs (if too large):**
```bash
> /home/ubuntu/obsidian-vault-starter/logs/claude-remote.log
```

## Troubleshooting

**Session exists but Claude App won't connect:**
- Restart the server to get a fresh connection URL
- Check log for errors

**"Session already running" but no process:**
- Kill the tmux session: `tmux kill-session -t obsidian-remote`
- Start fresh: `./scripts/start-claude-remote.sh`

**Can't attach to tmux:**
- Make sure you're the ubuntu user
- Check session exists: `tmux ls`

**Process running but no tmux session:**
- This shouldn't happen, but if it does: kill Claude processes and restart
- Find PIDs: `pgrep -f "claude.*obsidian"`
- Kill: `kill <PIDs>`
- Restart: `./scripts/start-claude-remote.sh`

## Security Notes

- Remote Control connections are authenticated via Claude App
- QR codes/links expire after use
- Log files may contain sensitive project information
- Only the ubuntu user should run these scripts
