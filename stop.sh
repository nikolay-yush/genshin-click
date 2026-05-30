#!/bin/bash

set -e

SERVICE_NAME="genshin-click"

SYSTEMD_DIR="$HOME/.config/systemd/user"

systemctl --user stop $SERVICE_NAME.timer
systemctl --user disable $SERVICE_NAME.timer

systemctl --user stop $SERVICE_NAME.service

rm -f "$SYSTEMD_DIR/$SERVICE_NAME.timer"
rm -f "$SYSTEMD_DIR/$SERVICE_NAME.service"

systemctl --user daemon-reload
systemctl --user reset-failed

echo ""
echo "🛑 Timer removed and stopped!"
echo ""