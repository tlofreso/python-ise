from ise.api.authentication import Authentication
from ise.api.endpoint import Endpoint

host = "10.10.20.70"
un = "admin"
pw = "C1sco12345!"
port = 443

auth = Authentication(host=host, user=un, password=pw, port=port).login()

ise_endpoint = Endpoint(auth, host)

my_endpoint = ise_endpoint.get_endpoint("00:00:00:00:00:00")

print(my_endpoint)
