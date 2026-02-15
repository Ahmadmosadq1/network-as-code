from netmiko import ConnectHandler
from datetime import datetime
import getpass

password = getpass.getpass("Password: ")

ip_list = ["192.168.72.11","192.168.72.22", "192.168.72.33", "192.168.72.44"]

devices = []

backup_time = datetime.now().strftime("%d-%m-%y")
for ip in ip_list:

    device = {
        "device_type":"cisco_ios",
        "host": ip,
        "username":"ahmed",
        "password":password,
        "secret":password
    }
    devices.append(device)

for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()
    print(f"inititiating runnunf configuration on {device['host']}")
    sh_run = connection.send_command("show run")
    with open(f'{device['host']}_{backup_time}', 'w') as file:
        file.write(sh_run)
        print("Backup saved")
print("Backup proccess done successfully")
