from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import getpass
import json

password = getpass.getpass("Password: " )
ip_list = ["192.168.72.11","192.168.72.22", "192.168.72.33", "192.168.72.44"]

devices = []


for ip in ip_list:

    device = {
        "device_type":"cisco_ios",
        "host": ip,
        "username":"ahmed",
        "password":password,
        "secret":password
    }
    devices.append(device)

my_file = "config_file.cfg"

for each_device in devices:
    try:
        with ConnectHandler(**each_device) as connection:
             connection.enable()
             output = connection.send_config_from_file(my_file)
             output += connection.save_config()
    except NetmikoAuthenticationException:
        print(f"{each_device['host']} ...Authentication faild")

    except NetmikoTimeoutException:
        print(f"{each_device['host']} ...unreachable")
