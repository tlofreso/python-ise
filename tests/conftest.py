import pytest


@pytest.fixture
def test_devices():
    from csv import reader

    with open("test_data.csv", "r") as data:
        read = reader(data)
        test_data = list(read)
        test_data.pop(0)

    return test_data


@pytest.fixture
def test_connection():
    import json
    import os

    import urllib3

    from ise.api.endpoint import Endpoint

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    with open("config.json") as f:
        config = json.load(f)

    host = config["ERS_HOST"]
    un = config["ERS_USER"]
    pw = config["ERS_PASS"]

    connection = Endpoint(host, user=un, password=pw)

    return connection

