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
def test_connection_endpoints():
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


@pytest.fixture
def test_connection_endpoint_groups():
    import json
    import os

    import urllib3

    from ise.api.endpoint import EndpointGroup

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    with open("config.json") as f:
        config = json.load(f)

    host = config["ERS_HOST"]
    un = config["ERS_USER"]
    pw = config["ERS_PASS"]

    connection = EndpointGroup(host, user=un, password=pw)

    return connection


@pytest.fixture
def test_connection_anc_endpoints():
    import json
    import os

    import urllib3

    from ise.api.anc_endpoint import ANCEndpoint

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    with open("config.json") as f:
        config = json.load(f)

    host = config["ERS_HOST"]
    un = config["ERS_USER"]
    pw = config["ERS_PASS"]

    connection = ANCEndpoint(host, user=un, password=pw)

    return connection
