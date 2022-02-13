class Script:
    def __init__(self, driver=None) -> None:
        self.driver = driver

    def exec(self):
        self.driver.goto("https://www.microsoft.com/")
        print(self.driver.get_page().title())
        self.driver.ss()
