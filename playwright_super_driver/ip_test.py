from script import Script
import json


class IpTest(Script):
    def exec(self, response=None, option=None):
        self.driver.goto("https://httpbin.org/ip")
        body = self.driver.locator('body').inner_text()
        print(body)
        response["result"] = json.loads(body)
        self.driver.ss()
