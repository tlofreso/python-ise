""" Cisco ISE ERS API ANC (Adaptive Network Control) Endpoint Operations """

from ise.api.http_methods import HttpMethods


class ANCEndpoint(object):
    """ ISE ANC Endpoint Operations """

    def __init__(self, host, user, password, port=9060):
        """ Initialize ANC Endpoint object session params

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

    def get_anc_endpoint_by_id(self, id):
        """ Obtains an ANC Ednpoint by id """

        url = f"{self.base_url}ancendpoint/{id}"
        response = HttpMethods(self, url).request(
            "PUT", self.user, self.password, payload
        )
        return response

    def anc_endpoint_clear(self, mac=None, ip=None):
        """ Clears an ANC Endpoint Policy from an ANC Endpoint """

        if mac is None and ip is None:
            response = "No IP or MAC Address specified!"

        payload = {
            "OperationAdditionalData": {
                "additionalData": [
                    {"name": "macAddress", "value": mac},
                    {"name": "ipAddress", "value": ip},
                ]
            }
        }

        url = f"{self.base_url}ancendpoint/apply"
        response = HttpMethods(self, url).request(
            "PUT", self.user, self.password, payload
        )
        return response

    def anc_endpoint_apply(self, policy, mac=None, ip=None):
        """ Applies an ANC Endpoint Policy to an ANC Endpoint """

        if mac is None and ip is None:
            response = "No IP or MAC Address specified!"

        payload = {
            "OperationAdditionalData": {
                "additionalData": [
                    {"name": "macAddress", "value": mac},
                    {"name": "policyName", "value": policy},
                ]
            }
        }

        url = f"{self.base_url}ancendpoint/apply"
        response = HttpMethods(self, url).request(
            "PUT", self.user, self.password, payload
        )
        return response

    def get_all_anc_endpoints(self):
        """ Returns all anc endpoints """

        url = f"{self.base_url}ancendpoint"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_anc_endpoint_version(self):
        """ Obtains version information for ERS API (anc endpoint) """

        url = f"{self.base_url}ancendpoint/versioninfo"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response


class ANCEndpointBulk(object):
    pass
