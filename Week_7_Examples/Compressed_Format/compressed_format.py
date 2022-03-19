"""There is a chance that we can write YAML file in compressed format. It is very similar
to Python. Technically, YAML is superset of JSON. They look very similar to Python from data
structure point of view. The 'default_flow_style'  makes it with normal YAML file. Otherwise
it will be in the compressed format."""
import yaml

my_dict = {
    "router1": {
        "management_address": "10.10.10.1",
        "router_name": "Router1",
        "system_interface": "10.10.10.100",
        "bgp_peers": ["1.1.1.1", "2.2.2.2"]
    },
    "router2": {
        "management_address": "10.10.10.2",
        "router_name": "Router2",
        "system_interface": "10.10.10.101",
        "bgp_peers": ["1.1.1.2", "2.2.2.3"]
    }
}

compressed_output = "compressed_yaml_file.yml"
with open(compressed_output, "w") as writer:
    output = yaml.dump(my_dict, writer, default_flow_style=False)

normal_output = "normal_yaml_file.yml"
with open(normal_output, "w") as writer:
    output = yaml.dump(my_dict, writer, default_flow_style=True)
