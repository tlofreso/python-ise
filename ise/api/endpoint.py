""" Cisco ISE API Endpoint operations """

from ise.api.http_methods import HttpMethods
from ise.utils import Utilities
from ise.api.profilerprofile import ProfilerProfile


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

    def get_endpoint_by_name(self, name):
        """ Obtain details of an endpoint by the endpoint name """

        url = f"{self.base_url}endpoint/name/{name}"
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
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_rejected_endpoints(self):
        """ Obtains all rejected endpoints """

        url = f"{self.base_url}endpoint/getrejectedendpoints"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_all_endpoints(self):
        """ Obtains all endpoints """

        url = f"{self.base_url}endpoint"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_endpoint_version_info(self):
        """ Obtains version information for ERS API """

        url = f"{self.base_url}endpoint/versioninfo"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_endpoint_group_by_name(self, group_name):
        """ Obtain details of an endpoint group by the group name
        
        Args:
            name (str): The name of a device group

        Returns:
            result (dict): All data associated with a response (Endpoint Group Details)
        
        """

        url = f"{self.base_url}endpointgroup?filter=name.EQ.{group_name}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_endpoints_by_groupid(self, group_id):
        """ Obtain a dictionary of endpoints by their group ID
        
        Args:
            group_id (str): Endpoint Group ID in ISE

        Returns:
            result (dict): All data asoociated with a response (endpoints in provided group ID)
        
        """

        url = f"{self.base_url}endpoint?filter=groupId.EQ.{group_id}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_all_endpoint_groups(self):
        """ Obtains a dictionary of all valid endpoint groups """

        url = f"{self.base_url}endpointgroup"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def create_endpoint(
        self,
        mac,
        profile_name=None,
        group_name=None,
        endpoint_name=None,
        description=None,
    ):
        """ Creates a new endpoint in ISE """

        mac = Utilities.normalize_mac(mac)

        if group_name is None:
            staticGroupAssignment = False
            groupId = ""
        else:
            staticGroupAssignment = True
            groupIdPayload = self.get_endpoint_group_by_name(group_name)
            groupId = Utilities.get_id(name=groupIdPayload)

        if profile_name is None:
            staticProfileAssignment = False
            profileId = ""
        else:
            profiler = ProfilerProfile(
                host=self.host, user=self.user, password=self.password
            )
            staticProfileAssignment = True
            profileIdPayload = profiler.get_profilerprofile_by_name(profile_name)
            profileId = Utilities.get_id(name=profileIdPayload)

        if endpoint_name is None:
            endpoint_name = mac

        payload = {
            "ERSEndPoint": {
                "id": "",
                "name": endpoint_name,
                "description": description,
                "mac": mac,
                "profileId": profileId,
                "staticProfileAssignment": staticProfileAssignment,
                "groupId": groupId,
                "staticGroupAssignment": staticGroupAssignment,
                "portalUser": "",
                "identityStore": "",
                "identityStoreId": "",
                "customAttributes": {
                    "customAttributes": {"key1": "value1", "key2": "value2"}
                },
                "mdmAttributes": {
                    "mdmServerName": "",
                    "mdmReachable": False,
                    "mdmEnrolled": False,
                    "mdmComplianceStatus": False,
                    "mdmOS": "",
                    "mdmManufacturer": "",
                    "mdmModel": "",
                    "mdmSerial": "",
                    "mdmEncrypted": False,
                    "mdmPinlock": False,
                    "mdmJailBroken": False,
                    "mdmIMEI": "",
                    "mdmPhoneNumber": "",
                },
            }
        }

        url = f"{self.base_url}endpoint"
        response = HttpMethods(self, url).request(
            "POST", self.user, self.password, payload
        )
        return response

    def update_endpoint(
        self,
        mac,
        profile_name=None,
        group_name=None,
        endpoint_name=None,
        description=None,
    ):
        """ Updates an existing endpoint """

        mac = Utilities.normalize_mac(mac)

        # Gather original endpoint information
        my_id = self.get_endpoint_by_mac(mac=mac)
        my_id = Utilities.get_id(my_id)
        old_attrs = self.get_endpoint_by_id(id=my_id)

        old_name = old_attrs["json"]["ERSEndPoint"]["name"]
        old_description = old_attrs["json"]["ERSEndPoint"]["description"]
        old_profileId = old_attrs["json"]["ERSEndPoint"]["profileId"]
        old_group_assign = old_attrs["json"]["ERSEndPoint"]["staticGroupAssignment"]
        old_groupId = old_attrs["json"]["ERSEndPoint"]["groupId"]

        if group_name is None and old_group_assign == False:
            staticGroupAssignment = False
            groupId = ""
        elif group_name is None and old_group_assign == True:
            staticGroupAssignment = True
            groupId = old_groupId
        else:
            staticGroupAssignment = True
            groupIdPayload = self.get_endpoint_group_by_name(group_name)
            groupId = Utilities.get_id(name=groupIdPayload)

        if profile_name is None and len(old_profileId) == 0:
            staticProfileAssignment = False
            profileId = ""
        elif profile_name is None and len(old_profileId) > 0:
            profiler = ProfilerProfile(
                host=self.host, user=self.user, password=self.password
            )
            staticProfileAssignment = True
            profileId = old_profileId
        else:
            profiler = ProfilerProfile(
                host=self.host, user=self.user, password=self.password
            )
            staticProfileAssignment = True
            profileIdPayload = profiler.get_profilerprofile_by_name(profile_name)
            profileId = Utilities.get_id(name=profileIdPayload)

        if endpoint_name is None and len(old_name) == 0:
            endpoint_name = mac
        elif endpoint_name is None and len(old_name) > 0:
            enpoint_name = old_name

        payload = {
            "ERSEndPoint": {
                "id": my_id,
                "name": endpoint_name,
                "description": description,
                "mac": mac,
                "profileId": profileId,
                "staticProfileAssignment": staticProfileAssignment,
                "groupId": groupId,
                "staticGroupAssignment": staticGroupAssignment,
                "portalUser": "",
                "identityStore": "",
                "identityStoreId": "",
                "customAttributes": {
                    "customAttributes": {"key1": "value1", "key2": "value2"}
                },
            }
        }

        url = f"{self.base_url}endpoint/{my_id}"
        response = HttpMethods(self, url).request(
            "PUT", self.user, self.password, payload
        )
        return response

    def delete_endpoint(self, mac):
        """ Removes an endpoint """

        mac = Utilities.normalize_mac(mac)

        # Gather original endpoint information
        my_id = self.get_endpoint_by_mac(mac=mac)
        my_id = Utilities.get_id(my_id)

        url = f"{self.base_url}endpoint/{my_id}"
        response = HttpMethods(self, url).request("DELETE", self.user, self.password)
        return response

