from driver import PlaywrightSuperDriver
from remote_context_manager import sync_playwright_remote
import os


class PlaywrightRemoteDriver(PlaywrightSuperDriver):
    def run(self, script):
        script.driver = self
        args = self.args()
        ep = self.endpoint()
        with sync_playwright_remote(ep) as p:
            self.browser = p.chromium.launch(
                headless=False, downloads_path="/tmp", args=args)
            script.exec()
            self.browser.close()

    def endpoint(self):
        return os.getenv('WS_ENDPOINT', 'ws://127.0.0.1:8080/ws')
