from playwright.sync_api import sync_playwright
from playwright._impl._page import Page
import os
from pathlib import PurePath


class PlaywrightSuperDriver:
    def __init__(self) -> None:
        self.browser = None
        self.page = None

    def run(self, script, response=None, option=None):
        script.driver = self
        args = self.args()
        with sync_playwright() as p:
            self.browser = p.chromium.launch(
                headless=True, downloads_path="/tmp", args=args)
            script.exec(response, option)
            self.quit()

    def get_page(self) -> Page:
        if not self.page:
            self.page = self.browser.new_page()
        return self.page

    def goto(self, link):
        self.get_page().goto(link)

    def get(self, link):
        return self.goto(link)

    def screenshot(self, path):
        self.get_page().screenshot(path=path)

    def ss(self, name="ss.png"):
        self.screenshot(self.download_path(name))

    def download_path(self, file):
        return str(PurePath(self.downloads_dir(), file))

    def downloads_dir(self):
        dir = os.getenv('USER_DOWNLOAD_DIR', '/tmp')
        os.makedirs(dir, exist_ok=True)
        return dir

    def locator(self, locale):
        self.get_page().locator(locale)

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

    def quit(self):
        if self.browser:
            self.browser.close()
            self.browser = None
