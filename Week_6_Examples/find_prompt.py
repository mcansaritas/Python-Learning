""" There is an argument named expect_string. Normally when we send a command we are
looking into the router prompt. We can change this by adding this argument with regex.
Let's write some code and see how does it work. """

from netmiko import ConnectHandler

my_device = {"host": "192.168.74.201", "username": "admin", "password": "admin", "device_type": "alcatel_sros"}

ssh_connection = ConnectHandler(**my_device)  # This will create an SSH connection to router
router_prompt =ssh_connection.find_prompt()  # This will assign the router prompt to a variable

print(router_prompt)  # This will print out the router prompt

arp_output = ssh_connection.send_command("show router arp", expect_string="A:R1#")  # This will send the command "show router arp"
print(arp_output)  # This will print out the command's output.

"""Our router's prompt is A:R1# and by default when a command is sent, it is looking for the 
router prompt and understand the command is run. When we specify an expect_string it is looking
for that specific string. It can be regular expression. When we chance the except_string to
A:R2# we are not able to see the ARP output."""