"""There is a possibility that we can reference to a dictionary with similar notation with
Python. We are going to try write a BGP template with BGP neighbors different parameters.
Let's try to run it and see what is the outcome."""

import jinja2

bgp_variables = {"router1": {
    "group_name": "iBGP_Neighbors",
    "import_policy": "Import_Policy",
    "export_policy": "Export_Policy",
    "peer_as": 65535,
    "neighbor": "1.1.1.1",
    "ipv6_peering": True,
    "bfd_enable": True
    },
    "router2": {"group_name": "eBGP_Neighbors",
    "import_policy": "Import",
    "export_policy": "Export",
    "peer_as": 20000,
    "neighbor": "2.2.2.2",
    "ipv6_peering": False,
    "bfd_enable": False
    }
}

with open("complex_template.j2") as reader:
    bgp_template = reader.read()

bgp_template = jinja2.Template(bgp_template)
output = bgp_template.render(bgp_variables)

print(output)
