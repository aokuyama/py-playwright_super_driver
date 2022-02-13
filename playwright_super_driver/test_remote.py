from remote_driver import PlaywrightRemoteDriver
from script import Script

driver = PlaywrightRemoteDriver()
script = Script()
response = {}
option = {}
driver.run(script, response, option)
