"""When we send a command to a router, when the command is sent, the router need to
gather additonal information from the user. As an example, if you want to delete a
file from cf3, the router is looking for additional information."""

from netmiko import ConnectHandler

my_device = {"host": "192.168.74.201", "username": "admin", "password": "admin", "device_type": "alcatel_sros"}

# Above we created our dictionary with the information that we need to connect the router

ssh_connnection = ConnectHandler(**my_device)  # This will let us connect to the router
file_name = "bootlog_prev.txt"  # That is the file name that we can to delete
my_command = fr"file delete cf3:\{file_name}"  # That is the command that we want to send
print(my_command)  # We are checking if the command is correct or not

delete_file = ssh_connnection.send_command_timing(my_command)  # That is the line where we are sending the command

if r"(y/n)" in delete_file:
    delete_file += ssh_connnection.send_command_timing("y")

print(delete_file)

