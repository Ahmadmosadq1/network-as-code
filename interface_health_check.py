from netmiko import ConnectHandler
from getpass import getpass

# Ask once, reuse everywhere
#getpass allows you to type without echoing to the terminal
password = getpass("Password:")

device ={
        "device_type": "cisco_ios",
        "host": "192.168.241.2",
        "username": "ahmed",
        "password": password,
    }

commands = [
    "show ip interface brief",
]

connection = ConnectHandler(**device)

for cmd in commands:
    output = connection.send_command(cmd)
    #print(f"--- {cmd} ---")
    #to print only first 4 lines of output
    lines = output.splitlines()
    print("The interfaces down are\n")
    for line in lines:
        parts = line.split()
        if "down" in parts:
            print(parts[0])


