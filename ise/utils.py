import netaddr
import random

from netaddr import EUI, mac_unix_expanded
from xml.etree import ElementTree
from xml.etree.ElementTree import tostring
from xml.dom import minidom


class Utilities(object):
    """ Documentation """

    def normalize_mac(mac):
        """ Takes any valid MAC address and returns one formatted for the ERS API 
        
        Args:
            mac (str): MAC address

        Returns:
            mac (str): MAC address in unix_expanded format: '00:00:00:00:00:00'

        Raises:
            AddrFormatError: Invalid MAC Address

        """

        try:
            mac = EUI(mac)
            mac.dialect = mac_unix_expanded

        except netaddr.core.AddrFormatError as e:
            raise Exception(f"Invalid MAC Address! error: {e}")

        return str(mac)

    def get_id(name):
        """ Takes a name (group_name, profile_name, dvice_name) and returns the ID """

        my_id = name["json"]["SearchResult"]["resources"][0]["id"]

        return my_id

    def prettify(elem):
        rough_string = ElementTree.tostring(elem, "utf-8")
        reparsed = minidom.parseString(rough_string)
        return reparsed.toxml()


class TestingUtilities(object):
    """ Contains utilities for use with automated testing """

    def generate_macs(number):
        """ Returns a specified number of valid, random mac addresses 
            between 00:00:00:00:00:00 & 00:00:00:FF:FF:FF

            Args:
                number (int): An integer equal to the desired number of generated macs
        """

        macs = []
        i = number

        while i > 0:
            mac = [
                random.randint(0x00, 0x7F),
                random.randint(0x00, 0x7F),
                random.randint(0x00, 0x7F),
                random.randint(0x00, 0x7F),
                random.randint(0x00, 0xFF),
                random.randint(0x00, 0xFF),
            ]

            new_mac = ":".join(map(lambda x: "%02x" % x, mac))
            macs.append(new_mac)

            i -= 1

        return macs

    def generate_endpoints(number, create=False, connection=None):
        """ Generates a specified number of valid, random endpoints 
        
        Args:
            number (int): An integer equal to the desired number of endpoints
            create (bool): Defaults to False. If set to True, method will create endpoints in ISE
            connection (object): required for Endpoint Creation

        Returns:
            endpoints (list): Randomly generated endpoints in a list of lists

        """

        valid_groups = [
            "Sony-Device",
            "Cisco-Meraki-Device",
            "Apple-iDevice",
            "BlackBerry",
            "Android",
            "Axis-Device",
            "Juniper-Device",
            "Epson-Device",
            "Profiled",
            "Blacklist",
            "GuestEndpoints",
            "Synology-Device",
            "Vizio-Device",
            "Trendnet-Device",
            "RegisteredDevices",
            "Cisco-IP-Phone",
            "Unknown",
            "Workstation",
        ]
        people = [
            "George Washington",
            "John Adams",
            "Thomas Jefferson",
            "James Madison",
            "James Monroe",
            "John Quincy Adams",
            "Andrew Jackson",
            "Martin Van Buren",
            "William Henry Harrison",
            "John Tyler",
        ]
        devices = [
            "iphone",
            "blackberry",
            "pixel",
        ]

        endpoints = []
        i = number

        while i > 0:
            my_mac = TestingUtilities.generate_macs(1)[0]
            my_group = random.choice(valid_groups)
            my_desc = f"{random.choice(people)}'s {random.choice(devices)}"
            line = [my_mac, my_group, my_desc]
            endpoints.append(line)

            i -= 1

        if create == True:
            for e in endpoints:
                mac = e[0]
                group = e[1]
                desc = e[2]
                connection.create_endpoint(mac=mac, group_name=group, description=desc)

        return endpoints


class Validators(object):
    """ Validates input to ERS Operation methods """

    def check_anc_policy_actions(values):
        print(values)
        print(type(values))
        if type(values) is not list:
            raise TypeError()

        for value in values:
            if value not in ("QUARANTINE", "PORTBOUNCE", "SHUTDOWN"):
                raise ValueError()
        else:
            return values
