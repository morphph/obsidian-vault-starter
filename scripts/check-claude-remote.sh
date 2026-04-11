#!/bin/bash
# Check Claude Code Remote Control status for Obsidian project

PROJECT_DIR="/home/ubuntu/obsidian-vault-starter"
TMUX_SESSION="obsidian-remote"
LOG_FILE="$PROJECT_DIR/logs/claude-remote.log"

echo "=== Claude Code Remote Control Status ==="
echo "Project: $PROJECT_DIR"
echo ""

# Check tmux session
if tmux has-session -t "$TMUX_SESSION" 2>/dev/null; then
    echo "✓ tmux session: RUNNING ($TMUX_SESSION)"
else
    echo "✗ tmux session: NOT RUNNING"
fi

# Check Claude Code process
CLAUDE_PROCS=$(pgrep -f "claude.*obsidian" || true)
if [ -n "$CLAUDE_PROCS" ]; then
    echo "✓ Claude process: RUNNING (PIDs: $CLAUDE_PROCS)"
else
    echo "✗ Claude process: NOT RUNNING"
fi

# Check log file
if [ -f "$LOG_FILE" ]; then
    echo "✓ Log file: $LOG_FILE"
    LOG_SIZE=$(du -h "$LOG_FILE" | cut -f1)
    LOG_LINES=$(wc -l < "$LOG_FILE")
    echo "  Size: $LOG_SIZE, Lines: $LOG_LINES"
    echo ""
    echo "--- Last 30 lines of log ---"
    tail -n 30 "$LOG_FILE"
else
    echo "✗ Log file not found"
fi

echo ""
echo "--- Overall Status ---"
if tmux has-session -t "$TMUX_SESSION" 2>/dev/null && [ -n "$CLAUDE_PROCS" ]; then
    echo "Status: HEALTHY"
    exit 0
elif tmux has-session -t "$TMUX_SESSION" 2>/dev/null || [ -n "$CLAUDE_PROCS" ]; then
    echo "Status: PARTIAL (session or process exists but not both)"
    exit 1
else
    echo "Status: NOT RUNNING"
    exit 2
fi
