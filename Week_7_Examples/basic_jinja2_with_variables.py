"""In the fist example, our dictionary was empty and directly Jinja2 template is printed out.
Right now, we are going to write a dictionary with needed information. Template variables are
written with  {{ }}. Let's write some code and see how does it work."""

# Let's create our dictionary first with for template.

import jinja2

bgp_variables = {
    "group_name": "iBGP",
    "neighbor_ip": "192.168.1.1",
    "import_policy": "Import_Policy",
    "export_policy": "Export_Policy",
    "peer_as": 2000
}

jinja2_template = """
    bgp
        group {{group_name}}
            family ipv4
            type external
            neighbor {{neighbor_ip}}
                import {{import_policy}}
                export {{export_policy}}
                peer-as {{peer_as}}
            exit
"""

bgp_template = jinja2.Template(jinja2_template)
output = bgp_template.render(bgp_variables)

print(output)

"""In this example, we can see that variables for our BGP template is written into a dictionary.
The variables are written into template with {{ }}. We can see that our variable values are in 
the output. We got the expected output."""

