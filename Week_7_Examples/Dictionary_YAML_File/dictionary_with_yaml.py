"""We are going to learn how we can create a dictionary with YAML. We need to write into our
YAML file a key and its value. It is simple as that. Let's try this with Python. Normally we
don't quote strings. If it is needed we can do it. We can indicate Booleans as well."""

import yaml

yaml_file1 = "dictionary_with_yaml.yml"
with open(yaml_file1) as reader:
    output = yaml.full_load(reader)

print(output)

"""We can see that the output is a dictionary. Also we have a chance to create a nested dictionary
as well. For that we need to use indentation."""

yaml_file2 = "nested_dictionary.yml"
with open(yaml_file2) as reader:
    output = yaml.full_load(reader)

print(output)
