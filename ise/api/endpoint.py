""" Cisco ISE API Endpoint operations """

# from ise.api.authentication import Authentication
from ise.api.http_methods import HttpMethods
from ise.utils import Utilities


class Endpoint(object):
    """ ISE Endpoint and Endpoint Group CRUD operations   
    
    """

    def __init__(self, host, user, password, port=9060):
        """ Initialize endpoint object session params
        
        Args:
            session (obj): Requests session object
            host (str): hostname or IP address of ISE
            port (int): defaults to ERS 9060 port
        
        """

        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.base_url = f"https://{self.host}:{self.port}/ers/config/"

    def get_endpoint_by_mac(self, mac):
        """ Obtain details of an endpoint by the MAC address
        
        Args:
            mac (str): MAC address of the endpoint

        Returns:
            result (dict): All data associated with a response (Endpoint Details)
            
        """
        mac = Utilities.normalize_mac(mac)

        url = f"{self.base_url}endpoint?filter=mac.EQ.{mac}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_endpoint_by_id(self, id):
        """ Obtain details of an endpoint by the endpoint ID
        
        Args:
            id (str): Endpoint ID In ISE

        Returns:
            result (dict): All data associated with a response (Endpoint Details)
        
        """

        url = f"{self.base_url}endpoint/{id}"
        response = HttpMethods(self.session, url).request("GET")
        return response

    def get_endpoint_group_by_name(self, group_name):
        """ Obtain details of an endpoint group by the group name
        
        Args:
            name (str): The name of a device group

        Returns:
            result (dict): All data associated with a response (Endpoint Group Details)
        
        """

        url = f"{self.base_url}endpointgroup?filter=name.EQ.{group_name}"
        response = HttpMethods(self.session, url).request("GET")
        return response

    def get_endpoints_by_groupid(self, group_id):
        """ Obtain a dictionary of endpoints by their group ID
        
        Args:
            group_id (str): Endpoint Group ID in ISE

        Returns:
            result (dict): All data asoociated with a response (endpoints in provided group ID)
        
        """

        url = f"{self.base_url}endpoint?filter=groupId.EQ.{group_id}"
        response = HttpMethods(self.session, url).request("GET")
        return response
