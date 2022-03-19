"""We can see that there are some repeating patterns inside our template. It would be nice if
we can use loops here. Jinja2 has an ability to use 'for' loops. We have 2 neighbor under the
BGP group. We can use them with 'for' loops."""

# Let's create a list which includes our BGP neighbors.

import jinja2

bgp_neighbors = ["1.1.1.1", "2.2.2.2"]

bgp_variables = {
    "group_name" : "iBGP_Neighbors",
    "import_policy": "Import_Policy",
    "export_policy": "Export_Policy",
    "peer_as": 65535,
    "bgp_neighbor": bgp_neighbors
}

template_file = "jinja_template_for_loop.j2"
with open(template_file) as reader:
    bgp_template = reader.read()

bgp_template = jinja2.Template(bgp_template)
output = bgp_template.render(bgp_variables)

print(output)

"""For Jinja2 template white spacing is an issue. For that we need to understand how the white
space is working for Jinja2."""
