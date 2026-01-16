from netmiko import ConnectHandler
from getpass import getpass

# Ask once, reuse everywhere
#getpass allows you to type without echoing to the terminal
password = getpass("Device Password:")

device ={
        "device_type": "cisco_ios",
        "host": "192.168.241.2",
        "username": "ahmed",
        "password": password,
    }

commands = [
    "show ip interface brief",
    "show version"
]

connection = ConnectHandler(**device)

for cmd in commands:
    output = connection.send_command(cmd)
    print(f"--- {cmd} ---")
    #to print only first 4 lines of output
    lines = output.splitlines()
    for line in lines:
        if line.startswith("GigabitEthernet0/0") and line.count("up") >= 2:  # Avoid printing empty lines
            print(line)
            

connection.disconnect()

