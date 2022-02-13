class Script:
    def __init__(self, driver=None) -> None:
        self.driver = driver

    def exec(self, response=None, option=None):
        self.driver.goto("https://www.microsoft.com/")
        print(self.driver.get_page().title())
        response["title"] = self.driver.get_page().title()
        self.driver.ss()
