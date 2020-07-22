from ise.api.endpoint import Endpoint

from csv import reader

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

with open("test_data.csv", "r") as data:
    read = reader(data)
    test_data = list(read)
    test_data.pop(0)


def test_create_endpoint():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    mac = test_data[0][0]
    group = test_data[0][1]
    desc = test_data[0][2]
    my_test = connection.create_endpoint(mac=mac, group_name=group, description=desc)

    assert my_test["status_code"] == 201


def test_update_endpoint():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    mac = test_data[0][0]
    group = test_data[0][1]
    desc = test_data[0][2]
    my_test = connection.update_endpoint(
        mac=mac, group_name=group, description=desc, endpoint_name="AdamsPhone"
    )

    assert my_test["status_code"] == 200


def test_delete_endpoint():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    mac = test_data[0][0]
    my_test = connection.delete_endpoint(mac=mac)

    assert my_test["status_code"] == 204


def test_get_endpoint_by_mac():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    my_test = connection.get_endpoint_by_mac(test_data[0][0])
    assert my_test["status_code"] == 200
