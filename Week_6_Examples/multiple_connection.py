"""There is a possibility that we may need to run the same command for multiple devices.
In this case we need to create a simple 'for' loop and send the command to the relevant
routers."""

from netmiko import ConnectHandler

my_device1 = {"host": "192.168.74.201", "username": "admin", "password": "admin", "device_type": "alcatel_sros"}
my_device2 = {"host": "192.168.74.201", "username": "admin", "password": "admin", "device_type": "alcatel_sros"}
my_list = [my_device1, my_device2]

# Above we have created 2 dictionaries for the router that we need to send the command.

for devices in my_list:
    ssh_connection = ConnectHandler(**devices)
    output = ssh_connection.send_command("show chassis")
    print(output)
    print("*"*30)