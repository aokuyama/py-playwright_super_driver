from remote_driver import PlaywrightRemoteDriver
from script import Script

driver = PlaywrightRemoteDriver()
script = Script()

driver.run(script)
