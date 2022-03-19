"""In this example, we are going to use JSON as an input for Jinja2. First, we are going to
read our JSON file, and bind in to a variable named dictionary. Then, we are going to read
our Jinja2 template and render the data with the template. It is again dictionary is the
variable that we are sending into Jinja2. All data we need is inside this dictionary
variable."""

import jinja2
import json

json_file = "complex_template_dictionary_looping_json.json"
with open(json_file) as reader:
    dictionary = json.load(reader)

print(dictionary)

jinja_template = "complex_template_dictionary_looping_json.j2"
with open(jinja_template) as reader:
    jinja_template = reader.read()

bgp_template = jinja2.Template(jinja_template)
output = bgp_template.render(dictionary)

print(output)
