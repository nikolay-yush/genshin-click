# Genshin Hoyolab Auto Claim

Simple Playwright automation script for claiming daily Hoyolab rewards.

## Installation

Install Python 3.12 and the uv package manager on your OS.

Run the following command to install all required packages:

```bash
uv sync
```

Create a `.env` file and replace `YOUR_ID` with your own ID:

```env
GENSHIN_DAILY_TASK_URL="https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=YOUR_ID&lang=ru-ru"
ICON_CHECK_SELECTOR="//div[contains(@class, 'actived-day')]/parent::*"
CHROME_EXECUTABLE_PATH="/usr/bin/google-chrome"
```

## First Run

Run the script manually:

```bash
python main.py
```

Log in to your account in the opened Chrome window.

---

## Scheduler

Make the scripts executable:

```bash
chmod +x start.sh
chmod +x stop.sh
```

Start the scheduler:

```bash
./start.sh
```

Stop the scheduler:

```bash
./stop.sh
```

---

## Useful Commands

Check timer status:

```bash
systemctl --user status genshin-click.timer
```

View logs:

```bash
journalctl --user -u genshin-click.service -f
```

Run the service manually:

```bash
systemctl --user start genshin-click.service


```
