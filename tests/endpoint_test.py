from ise.api.endpoint import Endpoint

import urllib3
import json
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("config.json") as f:
    config = json.load(f)

host = config["ERS_HOST"]
un = config["ERS_USER"]
pw = config["ERS_PASS"]

connection = Endpoint(host, user=un, password=pw)


def test_get_endpoint_by_mac():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    my_test = connection.get_endpoint_by_mac("00:00:00:00:00:00")

    assert my_test["status_code"] == 200
