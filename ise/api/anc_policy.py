""" Cisco ISE ERS API ANC (Adaptive Network Control) Policy Operations """

from ise.api.http_methods import HttpMethods
from ise.utils import Validators


class ANCPolicy(object):
    """ ISE ANC Policy Operations """

    def __init__(self, host, user, password, port=9060):
        """ Initialize ANC Policy object session params

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

    def get_anc_policy_by_name(self, name):
        """ Obtain details of a policy by the policy name """

        url = f"{self.base_url}ancpolicy/name/{name}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_anc_policy_by_id(self, id):
        """ Obtain details of a policy by the policy id """

        url = f"{self.base_url}ancpolicy/{id}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def update_anc_policy(self, id, actions):
        """ Updates a given ANC Policy """

        Validators.check_anc_policy_actions(value=actions)

        payload = {"ErsAncPolicy": {"name": id, "actions": [actions]}}

        url = f"{self.base_url}ancpolicy/{id}"
        response = HttpMethods(self, url).request(
            "PUT", self.user, self.password, payload
        )
        return response

    def delete_anc_policy(self, id):
        """ Deletes an ANC policy by ID """

        url = f"{self.base_url}ancpolicy/{id}"
        response = HttpMethods(self, url).request("DELETE", self.user, self.password)
        return response

    def create_anc_policy(self, name, actions):

        Validators.check_anc_policy_actions(value=actions)

        payload = {"ErsAncPolicy": {"name": name, "actions": [actions]}}

        url = f"{self.base_url}ancpolicy"
        response = HttpMethods(self, url).request(
            "POST", self.user, self.password, payload
        )
        return response

    def get_all_anc_policies(self):
        """ Gets all ANC Policies """

        url = f"{self.base_url}ancpolicy"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_anc_policy_version(self):
        """ Gets ANC Policy Version """

        url = f"{self.base_url}ancpolicy/versioninfo"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response
