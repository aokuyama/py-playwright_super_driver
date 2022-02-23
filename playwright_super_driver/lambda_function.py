from driver import PlaywrightSuperDriver
from script import Script
from lambda_util import setup_bin, cleanup
import json


def lambda_handler(event, context):
    setup_bin()

    driver = PlaywrightSuperDriver()
    script = Script()
    response = {}
    option = {}
    driver.run(script, response, option)
    cleanup()
    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }
