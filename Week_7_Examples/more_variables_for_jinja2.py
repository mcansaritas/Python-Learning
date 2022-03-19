"""We are going to include more variables in our dictionary used for Jinja2. We are going to
update our template a little and add a second BGP neighbor. Our BGP variables will be included
in our dictionary. Let's write the code and see how does it work."""

import jinja2

bgp_variables = {
    "group_name": "iBGP",
    "neighbor_ip1": "192.168.2.1",
    "neighbor_ip2": "192.168.3.1",
    "import_policy1": "Import_Policy",
    "export_policy1": "Export_Policy",
    "import_policy2": "Import",
    "export_policy2": "Export",
    "peer_as1": 1000,
    "peer_as2": 3000
}

jinja2_template = """
    bgp
        group {{group_name}}
            family ipv4
            type external
            neighbor {{neighbor_ip1}}
                import {{import_policy1}}
                export {{export_policy1}}
                peer-as {{peer_as1}}
            exit
            neighbor {{neighbor_ip2}}
                import {{import_policy2}}
                export {{export_policy2}}
                peer-as {{peer_as2}}
            exit
"""

bgp_template = jinja2.Template(jinja2_template)
output = bgp_template.render(bgp_variables)

print(output)
