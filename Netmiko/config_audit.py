from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import getpass

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

for device in devices:
    connection = ConnectHandler(**device)
    connection.enable()
    audited_command = connection.send_command("sh run")


    filename = f'{device['host']}.cfg'

    # creating a file and write the result of the command
    with open (filename, 'w') as f:
        f.write(audited_command)

    with open(filename,'r') as f:
        reader = f.read()

    if "ntp server 192.0.2.10" in reader:
        print(f"{device['host']} has NTP configured")
    else:
        print(f'WARNING!!!!!!!{device['host']} is Not configured')



