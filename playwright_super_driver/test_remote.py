from remote_driver import PlaywrightRemoteDriver
from ip_test import IpTest

driver = PlaywrightRemoteDriver()
script = IpTest()
response = {}
option = {}
driver.run(script, response, option)
