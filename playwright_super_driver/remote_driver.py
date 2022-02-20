from driver import PlaywrightSuperDriver
from remote_context_manager import sync_playwright_remote
import os
import traceback


class PlaywrightRemoteDriver(PlaywrightSuperDriver):
    def run(self, script, response=None, option=None):
        script.driver = self
        ep = self.endpoint()
        with sync_playwright_remote(ep) as playwright:
            self.playwright = playwright
            try:
                script.exec(response, option)
            except Exception as e:
                self.dying()
                raise e
            self.quit()

    def is_headless(self):
        return False

    def endpoint(self):
        return os.getenv('WS_ENDPOINT', 'ws://127.0.0.1:8080/ws')

    def user_data_dir(self):
        return os.getenv('REMOTE_USER_SESSION_DIR', '/tmp')
