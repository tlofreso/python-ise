""" Cisco ISE ERS API Endpoint operations """

from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from xml.etree import ElementTree
from xml.dom import minidom

from io import BytesIO
import os

from ise.api.http_methods import HttpMethods
from ise.utils import Utilities
from ise.api.profiler_profile import ProfilerProfile


class EndpointGroup(object):
    """ ISE Endpoint Group CRUD operations   
    
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
        self.base_url = f"https://{self.host}:{self.port}/ers/config/endpointgroup"

    def get_endpoint_group_by_name(self, group_name):
        """ Obtain details of an endpoint group by the group name
        
        Args:
            name (str): The name of a device group

        Returns:
            result (dict): All data associated with a response (Endpoint Group Details)
        
        """

        url = f"{self.base_url}?filter=name.EQ.{group_name}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_all_endpoint_groups(self):
        """ Obtains a dictionary of all valid endpoint groups """

        url = f"{self.base_url}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response


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
        self.base_url = f"https://{self.host}:{self.port}/ers/config/endpoint"

    def get_endpoint_by_mac(self, mac):
        """ Obtain details of an endpoint by the MAC address
        
        Args:
            mac (str): MAC address of the endpoint

        Returns:
            result (dict): All data associated with a response (Endpoint Details)
            
        """
        mac = Utilities.normalize_mac(mac)

        url = f"{self.base_url}?filter=mac.EQ.{mac}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_endpoint_by_name(self, name):
        """ Obtain details of an endpoint by the endpoint name """

        url = f"{self.base_url}/name/{name}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_endpoint_by_id(self, id):
        """ Obtain details of an endpoint by the endpoint ID
        
        Args:
            id (str): Endpoint ID In ISE

        Returns:
            result (dict): All data associated with a response (Endpoint Details)
        
        """

        url = f"{self.base_url}/{id}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_rejected_endpoints(self):
        """ Obtains all rejected endpoints """

        url = f"{self.base_url}/getrejectedendpoints"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_all_endpoints(self):
        """ Obtains all endpoints """

        url = f"{self.base_url}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_endpoint_version_info(self):
        """ Obtains version information for ERS API (endpoint) """

        url = f"{self.base_url}/versioninfo"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_endpoints_by_groupid(self, group_id):
        """ Obtain a dictionary of endpoints by their group ID
        
        Args:
            group_id (str): Endpoint Group ID in ISE

        Returns:
            result (dict): All data asoociated with a response (endpoints in provided group ID)
        
        """

        url = f"{self.base_url}?filter=groupId.EQ.{group_id}"
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
            grouper = EndpointGroup(
                host=self.host, user=self.user, password=self.password
            )
            staticGroupAssignment = True
            groupIdPayload = grouper.get_endpoint_group_by_name(group_name)
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

        url = f"{self.base_url}"
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
            grouper = EndpointGroup(
                host=self.host, user=self.user, password=self.password
            )
            staticGroupAssignment = True
            groupIdPayload = grouper.get_endpoint_group_by_name(group_name)
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

        url = f"{self.base_url}/{my_id}"
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

        url = f"{self.base_url}/{my_id}"
        response = HttpMethods(self, url).request("DELETE", self.user, self.password)
        return response


class EndpointBulk(object):
    """ ISE Endpoint and Endpoint Group Bulk CRUD operations """

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
        self.base_url = (
            f"https://{self.host}:{self.port}/ers/config/endpoint/bulk/submit"
        )

    def create_endpoint_bulk(self):
        """ Creates a batch of endpoints using bulk method """

        root = Element(
            "ns4:endpointBulkRequest",
            {
                "operationType": "create",
                "resourceMediaType": "vnd.com.cisco.ise.identity.endpoint.1.0+xml",
                "xmlns:ns6": "sxp.ers.ise.cisco.com",
                "xmlns:ns5": "trustsec.ers.ise.cisco.com",
                "xmlns:ns8": "network.ers.ise.cisco.com",
                "xmlns:ns7": "anc.ers.ise.cisco.com",
                "xmlns:ers": "ers.ise.cisco.com",
                "xmlns:xs": "http://www.w3.org/2001/XMLSchema",
                "xmlns:ns4": "identity.ers.ise.cisco.com",
            },
        )
        parent = SubElement(root, "ns4:resourcesList")

        child = SubElement(parent, "ns4:endpoint", {"description": "My Description"})
        mac = SubElement(child, "mac")
        mac.text = "00:00:00:00:00:00"

        # mdmAttributes = SubElement(child, "mdmAttributes")
        # mdmComplianceStatus = SubElement(mdmAttributes, "mdmComplianceStatus")
        # mdmEncrypted = SubElement(mdmAttributes, "mdmEncrypted")
        # mdmEnrolled = SubElement(mdmAttributes, "mdmEnrolled")
        # mdmIMEI = SubElement(mdmAttributes, "mdmIMEI")
        # mdmJailBroken = SubElement(mdmAttributes, "mdmJailBroken")
        # mdmManufacturer = SubElement(mdmAttributes, "mdmManufacturer")
        # mdmModel = SubElement(mdmAttributes, "mdmModel")
        # mdmOS = SubElement(mdmAttributes, "mdmOS")
        # mdmPhoneNumber = SubElement(mdmAttributes, "mdmPhoneNumber")
        # mdmPinLock = SubElement(mdmAttributes, "mdmPinLock")
        # mdmReachable = SubElement(mdmAttributes, "mdmReachable")
        # mdmSerial = SubElement(mdmAttributes, "mdmSerial")

        portalUser = SubElement(child, "portalUser")
        portalUser.text = "MyPortalUser"
        profileId = SubElement(child, "profileId")
        staticGroupAssignment = SubElement(child, "staticGroupAssignment")
        staticGroupAssignment.text = "false"
        staticProfileAssignment = SubElement(child, "staticProfileAssignment")
        staticProfileAssignment.text = "false"

        payload = ElementTree.tostring(root, method="html")
        print(payload)

        url = f"{self.base_url}"
        response = HttpMethods(self, url).request(
            "PUT",
            self.user,
            self.password,
            payload,
            headers={"Content-Type": "application/xml"},
        )
        return response
