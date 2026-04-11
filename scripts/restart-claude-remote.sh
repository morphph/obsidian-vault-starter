#!/bin/bash
# Restart Claude Code Remote Control for Obsidian project

set -e

PROJECT_DIR="/home/ubuntu/obsidian-vault-starter"
TMUX_SESSION="obsidian-remote"

echo "=== Restarting Claude Code Remote Control ==="

# Stop existing session if it exists
if tmux has-session -t "$TMUX_SESSION" 2>/dev/null; then
    echo "Stopping existing session '$TMUX_SESSION'..."
    tmux kill-session -t "$TMUX_SESSION"
    echo "✓ Stopped"
    sleep 2
else
    echo "No existing session to stop"
fi

# Start new session
echo ""
exec "$PROJECT_DIR/scripts/start-claude-remote.sh"
