class Script:
    def __init__(self, driver=None) -> None:
        self.driver = driver

    def exec(self):
        self.driver.goto("https://google.com")
        self.driver.ss()
