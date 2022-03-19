"""In this example, we are going to use CSV as an input for Jinja2. First, we are going to
read our CSV file. When we read our file, it will be a single dictionary with key/value pairs.
If there is any element that we want to split, we can split. In this example we split our BGP
neighbors and bind it back to the dictionary. Then, we are going to use our Jinja2 template to
render the configuration template."""

import csv
import jinja2

csv_file = "complex_jinja2_template_dictionary_looping_csv.csv"
with open(csv_file) as reader:
    dictionary = csv.DictReader(reader)
    for elements in dictionary:
        neighbors = elements["neighbors"]
        neighbors = neighbors.split()
        elements["neighbors"] = neighbors
        template_file = "complex_template_dictionary_looping_csv.j2"
        with open(template_file) as read:
            bgp_template = read.read()
        bgp_template = jinja2.Template(bgp_template)
        output = bgp_template.render(elements)
        print(output)
