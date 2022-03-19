"""After Jinja2, we are going to learn about YAML. It is highly readable and we can use with
Ansible as well. YAML files are created with '--' and each element is shown with '-'. YAML
returns a list of elements. Let's run some code and see how YAML works."""
import yaml

yaml_file = "basic_yaml_template.yml"
with open(yaml_file) as reader:
    output = yaml.full_load(reader)

print(output)

# We can see that the output is a list. As you know we can use indexing with lists.