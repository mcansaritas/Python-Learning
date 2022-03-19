from netmiko import ConnectHandler  # We need to import Netmiko first

def remote_connection(host, username, password, device_type):
    router_dictionary = {"host": host, "username": username, "password":password, "device_type":device_type}
    ssh_connection = ConnectHandler(**router_dictionary)
    command = ['configure router interface "system" address 10.10.10.10/32']
    router_interface = ssh_connection.send_command("show router interface", use_textfsm=True)
    for index, dictionary in enumerate(router_interface):
        if dictionary.get("interface") == "system" and dictionary.get("address")[0] == "10.10.10.1/32":
            ssh_connection.send_config_set(config_commands=command)
            break
    return

remote_connection("192.168.74.201", "admin", "admin", "alcatel_sros")
