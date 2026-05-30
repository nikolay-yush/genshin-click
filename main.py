from pathlib import Path
from datetime import datetime
from dotenv import set_key

from playwright.sync_api import (
    sync_playwright,
    BrowserContext,
    TimeoutError,
)

from settings import settings


STEALTH_SCRIPT = """
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
});

const getParameter = WebGLRenderingContext.prototype.getParameter;

WebGLRenderingContext.prototype.getParameter = function(parameter) {
    if (parameter === 37445) return 'NVIDIA';
    if (parameter === 37446) return 'GeForce GTX 1080';
    return getParameter(parameter);
};
"""


class Browser:

    def __init__(self):
        self.playwright = None
        self.context = None

    def start(self) -> BrowserContext:
        user_data_dir = Path("./chrome-profile").resolve()

        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=str(user_data_dir),
            executable_path=settings.CHROME_EXECUTABLE_PATH,
            headless=False,
            viewport=None,
            locale="ru-RU",
            timezone_id="Europe/Kiev",
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized",
                "--disable-dev-shm-usage",
                "--new-window",
            ],
        )

        self.context.add_init_script(STEALTH_SCRIPT)

        return self.context

    def stop(self):
        if self.context:
            self.context.close()

        if self.playwright:
            self.playwright.stop()


def main():
    browser = Browser()

    try:
        now = datetime.now()

        context = browser.start()

        page = context.new_page()

        page.goto(
            settings.GENSHIN_DAILY_TASK_URL,
            wait_until="domcontentloaded",
            timeout=20000,
        )

        if settings.FIRST_RUN:
            input("Press Enter to continue...")
            set_key(".env", "FIRST_RUN", "false")


        page.wait_for_timeout(5000)

        element = page.locator(f"xpath={settings.ICON_CHECK_SELECTOR}").first

        if element.is_visible():
            print(
                f"✅ Element found! "
                f"{now.strftime('%d.%m.%Y %H:%M:%S')}"
            )

            element.hover()

            page.wait_for_timeout(500)

            element.click()

            page.wait_for_timeout(1000)

            print("✅ Reward claimed!")

        else:
            print(
                f"❌ Element not found! "
                f"{now.strftime('%d.%m.%Y %H:%M:%S')}"
            )

        page.close()

    except TimeoutError:
        print(
            f"❌ Page load timeout! "
            f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}"
        )

    except Exception as error:
        print(
            f"❌ Error: {type(error).__name__} "
            f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}"
        )

        print(error)

    finally:
        browser.stop()


if __name__ == "__main__":
    main()