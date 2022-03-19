""" We are going to learn how we can use Jinja2 templates. First we need a set of variables.
And we are going to populate them in our configuration template and based on that we are going
to generate an output. It is the common serialization library. """

import jinja2

bgp_variables = {}  # We have created an empty dictionary.

jinja2_template = """  # This is the template that we are going to use for our template
    bgp
        group "BGP"
            family ipv4
            type external
            neighbor 172.23.109.24
                import "Import"
                export "Export"
                peer-as 100
            exit
"""

# Our dictionary is empty and no variables to write to template. So directly template will be printed.

bgp_template = jinja2.Template(jinja2_template)
output = bgp_template.render(bgp_variables)

print(output)

"""As you can see above, we have list of elements, specially for example it is empty dictionary.
We have a template that we are going to use. Then, using jinja2 we are importing our template,
then using this template we are rendering the data using the template, and get the output."""