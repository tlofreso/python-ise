import netaddr
import random
from netaddr import EUI, mac_unix_expanded


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
        print(my_id)

        return my_id


class TestingUtilities(object):
    """ Contains utilities for use with automated testing """

    def generate_macs(number):
        """ Returns a specified number of random mac addresses 
            between 00:00:00:00:00:00 & 00:00:00:FF:FF:FF

            Args:
                number (int): An integer equal to the desired number of generated macs
        """

        macs = []
        i = number

        while i > 0:
            mac = [
                0x00,
                0x00,
                0x00,
                random.randint(0x00, 0x7F),
                random.randint(0x00, 0xFF),
                random.randint(0x00, 0xFF),
            ]

            new_mac = ":".join(map(lambda x: "%02x" % x, mac))
            macs.append(new_mac)

            i -= 1

        return macs

