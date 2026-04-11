#!/bin/bash
# Start Claude Code Remote Control for Obsidian project
# This script creates a tmux session and runs Claude Code in remote control mode

set -e

PROJECT_DIR="/home/ubuntu/obsidian-vault-starter"
TMUX_SESSION="obsidian-remote"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/claude-remote.log"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Check if session already exists
if tmux has-session -t "$TMUX_SESSION" 2>/dev/null; then
    echo "✓ tmux session '$TMUX_SESSION' is already running"
    echo "  Attach with: tmux attach -t $TMUX_SESSION"
    exit 0
fi

# Create new tmux session and start Claude Code Remote Control server
echo "Starting Claude Code Remote Control server in tmux session '$TMUX_SESSION'..."

# Create tmux session and run the remote-control subcommand
# Auto-answer prompts: y (enable) and 1 (same-dir mode)
tmux new-session -d -s "$TMUX_SESSION" -c "$PROJECT_DIR" \
    "echo -e 'y\n1' | claude remote-control --name 'Obsidian' --permission-mode bypassPermissions --spawn same-dir 2>&1 | tee -a '$LOG_FILE'"

echo "✓ Started successfully"
echo "  Session: $TMUX_SESSION"
echo "  Log: $LOG_FILE"
echo "  Attach: tmux attach -t $TMUX_SESSION"
echo ""
echo "Note: Claude Code session is active and ready."
echo "      - Session name for Remote Control: starts with 'Obsidian'"
echo "      - Attach to session to view or interact"
echo "      - Use Claude App to connect via Remote Control"
