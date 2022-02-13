from driver import PlaywrightSuperDriver
from script import Script

driver = PlaywrightSuperDriver()
script = Script()
response = {}
option = {}
driver.run(script, response, option)
print(response)
