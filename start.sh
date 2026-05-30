#!/bin/bash

set -e

SERVICE_NAME="genshin-click"
SYSTEMD_DIR="$HOME/.config/systemd/user"

echo "📦 Copying systemd files..."

mkdir -p "$SYSTEMD_DIR"

cp "$SERVICE_NAME.service" "$SYSTEMD_DIR/"
cp "$SERVICE_NAME.timer" "$SYSTEMD_DIR/"

echo "🔄 Reloading systemd daemon..."
systemctl --user daemon-reload

echo "🧹 Reset failed state..."
systemctl --user reset-failed

echo "⏹ Restarting timer..."
systemctl --user disable --now "$SERVICE_NAME.timer" || true
systemctl --user enable --now "$SERVICE_NAME.timer"

echo ""
echo "✅ Timer started successfully!"
echo ""

systemctl --user list-timers | grep "$SERVICE_NAME"