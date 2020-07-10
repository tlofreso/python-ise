""" Cisco ISE API Endpoint operations """

from ise.api.http_methods import HttpMethods
from ise.api.authentication import Authentication
from ise.utils import Utilities


class Endpoint(object):
    """ ISE Endpoint and Endpoint Group CRUD operations   
    
    """

    def __init__(self, session, host, port=9060):
        """ Initialize endpoint object session params
        
        Args:
            session (obj): Requests session object
            host (str): hostname or IP address of ISE
            port (int): defaults to ERS 9060 port
        
        """

        self.session = session
        self.host = host
        self.port = port
        self.base_url = f"https://{self.host}:{self.port}/ers/config/"

    def get_endpoint_by_mac(self, mac):
        """ Obtain details of an endpoint by the MAC address
        
        Args:
            mac (str): MAC address of the device

        Returns:
            result (dict): All data associated with a response
            
        """
        print(mac)
        mac = Utilities.normalize_mac(mac)
        print(mac)

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
