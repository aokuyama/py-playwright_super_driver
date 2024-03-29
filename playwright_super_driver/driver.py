from playwright.sync_api import sync_playwright
from playwright._impl._page import Page
import os
from pathlib import PurePath
from locator_wrapper import Locator
import datetime


class PlaywrightSuperDriver:
    def __init__(self) -> None:
        self.playwright = None
        self.browser = None
        self.page = None

    def run(self, script, response=None, option=None):
        script.driver = self
        with sync_playwright() as playwright:
            self.playwright = playwright
            try:
                script.exec(response, option)
            except Exception as e:
                self.dying()
                self.quit()
                raise e
            self.quit()

    def get_page(self) -> Page:
        if not self.page:
            self.page = self.get_browser().new_page()
        return self.page

    def get_browser(self):
        if not self.browser:
            self.browser = self.launch_browser()
        return self.browser

    def launch_browser(self):
        args = self.args()
        dir = self.user_data_dir()
        proxy = self.proxy_args()
        user_agent = self.user_agent()
        return self.playwright.chromium.launch_persistent_context(dir, headless=self.is_headless(), downloads_path="/tmp", args=args, proxy=proxy, user_agent=user_agent)

    def is_headless(self):
        return True

    def goto(self, link):
        self.get_page().goto(link)

    def get(self, link):
        return self.goto(link)

    def go_back(self):
        self.get_page().go_back()

    def screenshot(self, path):
        self.get_page().screenshot(path=path)

    def ss(self, name="ss"):
        self.screenshot(self.download_path(name + '.png'))

    def dying(self):
        if self.browser and self.page:
            try:
                self.ss(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")))
            except Exception as e:
                print(e)

    def download_path(self, file):
        return str(PurePath(self.downloads_dir(), file))

    def downloads_dir(self):
        dir = os.getenv('USER_DOWNLOAD_DIR', '/tmp')
        os.makedirs(dir, exist_ok=True)
        return dir

    def get_page_url(self) -> str:
        return self.get_page().url

    def locator(self, selector: str) -> Locator:
        l = self.get_page().locator(selector)
        return Locator(l)

    def is_checked(self, selector: str) -> Locator:
        return self.get_page().is_checked(selector)

    def is_disabled(self, selector: str) -> Locator:
        return self.get_page().is_disabled(selector)

    def is_editable(self, selector: str) -> Locator:
        return self.get_page().is_editable(selector)

    def is_enabled(self, selector: str) -> Locator:
        return self.get_page().is_enabled(selector)

    def is_hidden(self, selector: str) -> Locator:
        return self.get_page().is_hidden(selector)

    def is_visible(self, selector: str) -> Locator:
        return self.get_page().is_visible(selector)

    def user_data_dir(self):
        dir = os.getenv('USER_SESSION_DIR', '/tmp')
        os.makedirs(dir, exist_ok=True)
        return dir

    def args(self):
        return [
            '--autoplay-policy=user-gesture-required',
            '--disable-background-networking',
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-breakpad',
            '--disable-client-side-phishing-detection',
            '--disable-component-update',
            '--disable-default-apps',
            '--disable-dev-shm-usage',
            '--disable-domain-reliability',
            '--disable-extensions',
            '--disable-features=AudioServiceOutOfProcess',
            '--disable-hang-monitor',
            '--disable-ipc-flooding-protection',
            '--disable-notifications',
            '--disable-offer-store-unmasked-wallet-cards',
            '--disable-popup-blocking',
            '--disable-print-preview',
            '--disable-prompt-on-repost',
            '--disable-renderer-backgrounding',
            '--disable-setuid-sandbox',
            '--disable-speech-api',
            '--disable-sync',
            '--disk-cache-size=33554432',
            '--hide-scrollbars',
            '--ignore-gpu-blacklist',
            '--metrics-recording-only',
            '--mute-audio',
            '--no-default-browser-check',
            '--no-first-run',
            '--no-pings',
            '--no-sandbox',
            '--no-zygote',
            '--password-store=basic',
            '--use-gl=swiftshader',
            '--use-mock-keychain',
            '--single-process'
        ]

    def proxy_args(self):
        host = os.getenv('PROXY_HOST')
        if not host:
            return None
        port = os.getenv('PROXY_PORT', '3128')
        username = os.getenv('PROXY_USER')
        password = os.getenv('PROXY_PASSWORD')
        args = {
            "server": host + ":" + port,
        }
        if username:
            args["username"] = username
        if password:
            args["password"] = password
        return args

    def user_agent(self):
        return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'

    def quit(self):
        if self.browser:
            self.browser.close()
            self.browser = None
