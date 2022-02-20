from driver import PlaywrightSuperDriver
from script import Script
from ip_test import IpTest

driver = PlaywrightSuperDriver()
script = Script()
script = IpTest()
response = {}
option = {}
driver.run(script, response, option)
print(response)
