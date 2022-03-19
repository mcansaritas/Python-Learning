"""Netmiko has a write channel and read channel method. We can use write channel to send some
commands to the remote end. We can use the read channel to understand the output back. Let' write
some code and see what can be the output."""

from netmiko import ConnectHandler
import time

my_device = {"host": "192.168.74.201", "username": "admin", "password": "admin", "device_type": "alcatel_sros"}

ssh_connnection = ConnectHandler(**my_device)  # This will let us connect to the router

ssh_connnection.write_channel("show system information\n")
time.sleep(3)
channel_read = ssh_connnection.read_channel()
print(channel_read)

ssh_connnection.disconnect()