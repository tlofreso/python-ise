""" Cisco ISE API Profiler Profile Operations """

from ise.api.http_methods import HttpMethods


class ProfilerProfile(object):
    """ ISE Profiler Profile Operations """

    def __init__(self, host, user, password, port=9060):
        """ Initialize Profiler Profile object session params

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

    def get_profilerprofile_by_id(self, id):
        """ Documentation """

        url = f"{self.base_url}profilerprofile/{id}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_all_profilerprofiles(self):
        """ Documentation """

        url = f"{self.base_url}profilerprofile"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_profilerprofile_version_info(self):
        """ Documentation """

        url = f"{self.base_url}profilerprofile/versioninfo"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response

    def get_profilerprofile_by_name(self, profile_name):
        """ Documentation """

        url = f"{self.base_url}/profilerprofile?filter=name.eq.{profile_name}"
        response = HttpMethods(self, url).request("GET", self.user, self.password)
        return response
