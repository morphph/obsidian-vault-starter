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

# Create new tmux session ready for Claude Code
echo "Creating tmux session '$TMUX_SESSION' for Claude Code..."

# Create tmux session and start Claude Code interactively
# The session will show a starting prompt and wait for Remote Control connection
tmux new-session -d -s "$TMUX_SESSION" -c "$PROJECT_DIR"

# Start Claude Code with a simple prompt to initialize the session
# Remove --chrome as it seems to cause issues
# The --remote-control-session-name-prefix allows Remote Control to find this session
tmux send-keys -t "$TMUX_SESSION" "claude --permission-mode bypassPermissions --remote-control-session-name-prefix Obsidian --name 'Obsidian Remote' 'Ready for Remote Control. This session is running and waiting for connections.'" C-m

echo "✓ Started successfully"
echo "  Session: $TMUX_SESSION"
echo "  Log: $LOG_FILE (currently not logging)"
echo "  Attach: tmux attach -t $TMUX_SESSION"
echo ""
echo "Note: Claude Code session is active and ready."
echo "      - Session name for Remote Control: starts with 'Obsidian'"
echo "      - Attach to session to view or interact"
echo "      - Use Claude App to connect via Remote Control"
