#!/bin/bash

set -e

SERVICE_NAME="genshin-click"

SYSTEMD_DIR="$HOME/.config/systemd/user"

mkdir -p "$SYSTEMD_DIR"

cp $SERVICE_NAME.service "$SYSTEMD_DIR/"
cp $SERVICE_NAME.timer "$SYSTEMD_DIR/"

systemctl --user daemon-reload

systemctl --user enable --now $SERVICE_NAME.timer

echo ""
echo "✅ Timer started!"
echo ""

systemctl --user status $SERVICE_NAME.timer