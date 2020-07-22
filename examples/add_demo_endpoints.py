import json
import pprint as pp
import os
import csv

from ise.utils import TestingUtilities
from ise.api.endpoint import Endpoint
from ise.api.profilerprofile import ProfilerProfile

with open("config.json") as f:
    config = json.load(f)

host = config["ERS_HOST"]
un = config["ERS_USER"]
pw = config["ERS_PASS"]

connection = Endpoint(host, user=un, password=pw)

demo_endpoints = TestingUtilities.generate_endpoints(30)

# for endpoint in demo_endpoints:
#     mac = endpoint[0]
#     group = endpoint[1]
#     description = endpoint[2]
#     connection.create_endpoint(mac=mac, group_name=group, description=description)


with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(demo_endpoints)
