"""Sometimes we need to send a command and we are going to do some config changes. For
this purpose we are going to use set_config_set method."""

from netmiko import ConnectHandler

my_device = {"host": "192.168.74.201", "username": "admin", "password": "admin", "device_type": "alcatel_sros"}
configuration_commands = ['configure router interface "system" address 10.10.10.1/32', 'configure router interface "toR2" shutdown']

ssh_connection = ConnectHandler(**my_device)
system_ip_change = ssh_connection.send_config_set(configuration_commands)
print(system_ip_change)