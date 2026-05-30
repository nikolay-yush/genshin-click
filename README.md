# Genshin Hoyolab Auto Claim

Simple Playwright automation for daily Hoyolab reward claim.

## Installation
install Python 3.12
install uv manager

create .env file with:

    GENSHIN_DAILY_TASK_URL=https://example.com
    ICON_CHECK_SELECTOR=div.actived-day

# First Run

Run script manually:

```bash
python main.py
```

Login to your account in opened Chrome window.

---

# Scheduler

Make scripts executable:

```bash
chmod +x start.sh
chmod +x stop.sh
```

Start scheduler:

```bash
./start.sh
```

Stop scheduler:

```bash
./stop.sh
```

---

# Useful Commands

Check timer status:

```bash
systemctl --user status genshin-click.timer
```

View logs:

```bash
journalctl --user -u genshin-click.service -f
```

Manual service run:

```bash
systemctl --user start genshin-click.service
```
