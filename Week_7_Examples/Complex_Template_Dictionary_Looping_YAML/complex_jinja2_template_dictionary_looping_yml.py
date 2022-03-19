"""In this example, we are going to use YAML as an input for Jinja2. First, we are going to
read our YAML file, and bind in to a variable named dictionary. Then, we are going to read
our Jinja2 template and render the data with the template. It is again dictionary is the
variable that we are sending into Jinja2. All data we need is inside this dictionary
variable."""

import jinja2
import yaml

yaml_file = "complex_template_dictionary_looping.yml"
with open(yaml_file) as reader:
    dictionary = yaml.full_load(reader)

jinja_file = "complex_template_dictionary_looping_yml.j2"
with open(jinja_file) as reader:
    template = reader.read()

template = jinja2.Template(template)
output = template.render(dictionary)

print(output)
