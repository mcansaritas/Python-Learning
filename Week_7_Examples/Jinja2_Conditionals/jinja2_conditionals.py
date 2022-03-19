"""In the first example with 'for' loops, we understand that the white spacing is a little
a problem. In this example, we are going to use 'for' loops, and at the same time we are going
to use conditionals with 'if' statements."""

# Let's create a list which includes our BGP neighbors.

import jinja2

# We have 2 BGP neighbors. One of the BGP peers will have IPv4 and IPv6 with bfd-enable config.
# The other one will have only IPv4 without bfd-enable configuration.

bgp_neighbors = ["1.1.1.1", "2.2.2.2"]

bgp_neighbor_variables = {
    "group_name": "iBGP_Neighbors",
    "import_policy": "Import_Policy",
    "export_policy": "Export_Policy",
    "peer_as": 65535,
    "bgp_neighbor": bgp_neighbors,
    "ipv6_peering": True,
    "bfd_enable": True
}

template_file = "jinja2_conditionals.j2"
with open(template_file) as reader:
    bgp_template = reader.read()

bgp_template = jinja2.Template(bgp_template)
output = bgp_template.render(bgp_neighbor_variables)

print(output)
