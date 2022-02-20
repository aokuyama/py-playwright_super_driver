from driver import PlaywrightSuperDriver
from ip_test import IpTest

driver = PlaywrightSuperDriver()
script = IpTest()
response = {}
option = {}
driver.run(script, response, option)
print(response)
