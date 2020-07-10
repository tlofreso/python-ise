""" Cisco ISE API Endpoint operations """

from ise.api.http_methods import HttpMethods
from ise.api.authentication import Authentication


class Endpoint(object):
    """ Documentation """

    def __init__(self, session, host, port=9060):
        """ Documentation """

        self.session = session
        self.host = host
        self.port = port
        self.base_url = f"https://{self.host}:{self.port}/ers/config/"

    def get_endpoint_by_mac(self, mac):
        """ Documentation """

        url = f"{self.base_url}endpoint?filter=mac.EQ.{mac}"
        response = HttpMethods(self.session, url).request("GET")
        return response

    def get_endpoint_by_id(self, id):
        """ Documentation """

        url = f"{self.base_url}endpoint/{id}"
        response = HttpMethods(self.session, url).request("GET")
        return response

    def get_endpoint_group_by_name(self, group_name):
        """ Documentation """

        url = f"{self.base_url}endpointgroup?filter=name.EQ.{group_name}"
        response = HttpMethods(self.session, url).request("GET")
        return response

    def get_endpoints_by_groupid(self, group_id):
        """ Documentation """

        url = f"{self.base_url}endpoint?filter=groupId.EQ.{group_id}"
        response = HttpMethods(self.session, url).request("GET")
        return response
