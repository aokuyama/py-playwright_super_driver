from driver import PlaywrightSuperDriver
from script import Script
from lambda_util import setup_bin


def lambda_handler(event, context):
    setup_bin()

    driver = PlaywrightSuperDriver()
    script = Script()
    driver.run(script)
    return {
        "statusCode": 200,
        "body": "",
    }
