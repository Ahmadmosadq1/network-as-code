from napalm import get_network_driver
import json

#creating an object. Napal is vendor neutral
#driver for cisco

driver = get_network_driver('ios')
ipaddr = '192.168.72.11'
username = 'ahmed'
password = '1111'
secret = '1111'

with driver(ipaddr, username, password, optional_args={"secret": secret}) as device:
    device.open()
    print(json.dumps(device.get_lldp_neighbors(), sort_keys=True))
