#!/bin/bash

set -e

SERVICE_NAME="genshin-click"
SYSTEMD_DIR="$HOME/.config/systemd/user"

echo "⛔ Stopping timer..."
systemctl --user stop "$SERVICE_NAME.timer" || true
systemctl --user disable "$SERVICE_NAME.timer" || true

echo "🧹 Reset failed state..."
systemctl --user reset-failed || true

echo "🗑 Removing systemd files..."
rm -f "$SYSTEMD_DIR/$SERVICE_NAME.timer"
rm -f "$SYSTEMD_DIR/$SERVICE_NAME.service"

echo "🔄 Reloading systemd..."
systemctl --user daemon-reload

echo ""
echo "✅ Fully uninstalled!"
echo ""