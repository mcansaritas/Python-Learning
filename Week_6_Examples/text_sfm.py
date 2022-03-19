"""Our output can be a one big string. This is undesirable. We need to extract the information
that we need from the output. So, we can use TextFSM for this purpose. We can see that it returns
a list, inside there are some dictionaries."""

from netmiko import ConnectHandler

my_device = {"host": "192.168.74.201", "username": "admin", "password": "admin", "device_type": "alcatel_sros"}

ssh_connection = ConnectHandler(**my_device)
router_interface = ssh_connection.send_command("show router interface", use_textfsm=True)
print(router_interface)  # This will print out a list and inside there are dictionaries

print("*"*30)

print(len(router_interface))  # This will print out 5 and this is the number of interfaces we have

print("*"*30)

print(router_interface[0].items())

print("*"*30)

print(router_interface[0]["interface"])  # This will print out the first dictionary's interface name