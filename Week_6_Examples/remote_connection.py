""" This is going to be our first SSH connection attempt that we are going to do with Pyhton.
First, we need to create a dictionary for our SSH connection. Our SSH connection information
needed for netmiko will be in the dictionary. We are going to use ConnectHandler to connect
to a router. """

from netmiko import ConnectHandler

my_device = {"host": "192.168.74.201", "username": "admin", "password": "admin", "device_type": "alcatel_sros"}

ssh_connection = ConnectHandler(**my_device)  # This will create an SSH connection

"""Above we are going use use **kwargs method. ConnectHandler is going to behave our dictionary
as key and value pairs, not as one element."""

router_interface = ssh_connection.send_command("show router interface")  # This command will print out all interfaces
print(router_interface)

print("*"*30)

system_interface = ssh_connection.send_command('show router interface "system"')  # This will print out system interface

print(system_interface)

