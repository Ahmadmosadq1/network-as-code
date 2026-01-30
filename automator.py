from netmiko import ConnectHandler
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")

routers = [
    {
        "device_type": "linux",
        "host": "172.20.100.11",
    },
    {
        "device_type": "linux",
        "host": "172.20.100.12",
    },
]

for r in routers:
    r["username"] = username
    r["password"] = password

    print(f"\n===== {r['host']} =====")

    conn = ConnectHandler(**r)

    output = conn.send_command("ip -br addr")
    # Cisco-style alternative:
    # output = conn.send_command("vtysh -c 'show ip interface brief'"

    print(output)

    conn.disconnect()
