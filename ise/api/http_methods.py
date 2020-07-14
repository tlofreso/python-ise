import json

import urllib3

import requests
from requests.auth import HTTPBasicAuth

DEFAULT_HEADERS = {"Content-type": "application/json", "Accept": "application/json"}
DEFAULT_TIMEOUT = 5
VALID_SUCCESS_CODES = [200, 201, 202, 204]
VALID_FAILURE_CODES = [400, 401, 403, 404, 415, 500]

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class HttpMethods(object):
    """ documentation """

    def __init__(self, session, url):
        """ documentation """

        self.session = session
        self.url = url

    def request(self, method, user, password, payload=None, headers=None):
        """ documentation """

        if headers is None:
            headers = DEFAULT_HEADERS
        result = {}
        error = None
        data = None
        details = None
        result_json = None

        try:
            response = requests.request(
                method,
                self.url,
                headers=headers,
                timeout=DEFAULT_TIMEOUT,
                verify=False,
                auth=HTTPBasicAuth(user, password),
                data=json.dumps(payload),
            )
            print(response)

        except requests.exceptions.ConnectionError as e:
            raise Exception(f"Connection error to {self.url}: {e}")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"An HTTP error occurred: {e}")
        except requests.exceptions.URLRequired as e:
            raise Exception(f"A valid URL is required to make a request: {e}")
        except requests.exceptions.TooManyRedirects as e:
            raise Exception(f"Too many redirects: {e}")
        except requests.exceptions.Timeout as e:
            raise Exception(f"The request timed out: {e}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"There was an ambiguous exception: {e}")

        if response.text:
            try:
                result_json = json.loads(response.text)
            except json.JSONDecodeError as e:
                raise Exception(f"Payload format error: {e}")

        result = {
            "status_code": response.status_code,
            "details": details,
            "error": error,
            "json": result_json,
            "response": response,
        }

        if response.status_code not in VALID_SUCCESS_CODES:
            if result_json and "error" in result_json:
                details = result_json["error"]["details"]
                error = result_json["error"]["message"]
                raise Exception(
                    f"{self.url}: Error {result['status_code']} ({result['status']}) - {error}: {details}"
                )
            else:
                raise Exception(print(result))
                # f"{self.url}: Error {result['status_code']} ({result['status']})"

        return result
