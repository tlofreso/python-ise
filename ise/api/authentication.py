# """ Cisco ISE API Authentication """
#
# import json
# import socket
#
# import requests
# import urllib3
# from requests.auth import HTTPBasicAuth
#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#
#
# class Authentication(object):
#     """ ISE API Authentication """
#
#     def __init__(
#         self,
#         host=None,
#         user=None,
#         password=None,
#         port=9060,
#         timeout=5,
#         validate_certs=False,
#     ):
#         """ Initialize API authentication with provided parameters.
#
#         Args:
#             host (str): hostname or IP address of ise
#             user (str): username for authentication
#             password (str): password for authentication
#             port (int): defaults to 9060
#             validate_certs (bool): cert validation true / fals
#             timeout (int): defaults to 5 seconds
#
#         """
#
#         self.host = host
#         self.user = user
#         self.password = password
#         self.port = port
#         self.timeout = timeout
#         self.verify = validate_certs
#         self.base_url = f"https://{self.host}:{self.port}/ers/config/node"
#
#         self.auth = HTTPBasicAuth(user, password)
#
#     def login(self):
#         """ Will login to ISE API, and return a useable session
#
#         Args:
#             None
#
#         Returns:
#             self.session
#
#         """
#         session = requests.request(
#             method="get",
#             url=self.base_url,
#             auth=self.auth,
#             headers={"Content-type": "application/json", "Accept": "application/json"},
#             verify=self.verify,
#         )
#
#         return session.text
#

