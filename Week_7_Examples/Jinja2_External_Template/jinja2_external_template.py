"""There is a chance that we can select not to include our Jinja2 template in our code. For that
we need to externally create our Jinja2 template. We are going to use our last example's template
that we have write. It will be only external to the code."""

import jinja2

bgp_variables = {
    "group_name": "iBGP",
    "neighbor_ip1": "192.168.20.1",
    "neighbor_ip2": "192.168.30.1",
    "import_policy1": "Import_Policy",
    "export_policy1": "Export_Policy",
    "import_policy2": "Import",
    "export_policy2": "Export",
    "peer_as1": 1000,
    "peer_as2": 3000
}

template_file = r"C:\Users\saritas\Python Projects\Kirk Byers Network Automation\Week_7_Examples\Jinja2_External_Template\jinja2_template.j2"
with open(template_file) as template:
    bgp_template = template.read()

bgp_template = jinja2.Template(bgp_template)
output = bgp_template.render(bgp_variables)

print(output)

"""We can see that we correctly read the template from external Jinja2 file. Then we printed out
the template that we need."""
