"""In this example we wanted to test our Jinja2 template with 'for' loops. There are some lessons
learned here. First we are going to use a dictionary for Jinja2 template. In this case, we are
going to send dictionary to the Jinja2. Inside the dictionary we are going to use dictionaries
for the routers that we have. We can loop them with 'for' loops inside Jinja2. That is how we
did it in this example. Variable dictionary is only used when sending the data to Jinja2."""

import jinja2

router1_neighbors = ["1.1.1.1", "2.2.2.2"]
router2_neighbors = ["1.1.1.2", "2.2.2.3"]

dictionary = {
    "routers": {
        "router1": {
            'group_name': 'iBGP Neighbors',
            'import_policy': 'Import_Policy',
            'export_policy': 'Export_Policy',
            'peer_as': 65535,
            'neighbor': router1_neighbors,
            'ipv6_peering': True,
            'bfd_enable': True},
        "router2": {
            'group_name': 'eBGP Neighbors',
            'import_policy': 'Import',
            'export_policy': 'Export',
            'peer_as': 2000,
            'neighbor': router2_neighbors,
            'ipv6_peering': False,
            'bfd_enable': False
        }
    }
}

jinja_template = "complex_template_dictionary_looping.j2"
with open(jinja_template) as reader:
    jinja_template = reader.read()

bgp_template = jinja2.Template(jinja_template)
output = bgp_template.render(dictionary)

print(output)
