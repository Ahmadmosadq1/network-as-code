import json
from napalm import get_network_driver


#creating an object. Napal is vendor neutral
#driver for cisco

driver = get_network_driver('ios')
ipaddr = '192.168.72.11'
username = 'ahmed'
password = '1111'
secret = '1111'

CONFIG_SNIPPET = """
 description suckaaa
"""

with driver(ipaddr, username, password, optional_args={"secret": secret}) as device:
    device.load_merge_candidate(config=CONFIG_SNIPPET)
    diff = device.compare_config()
    if diff:
        device.commit_config()
        print("config committed")
        device.discard_config()
    else:
        print("No change")

