from remote_driver import PlaywrightRemoteDriver
from script import Script
from ip_test import IpTest

driver = PlaywrightRemoteDriver()
script = Script()
script = IpTest()
response = {}
option = {}
driver.run(script, response, option)
