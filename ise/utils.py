import netaddr
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
