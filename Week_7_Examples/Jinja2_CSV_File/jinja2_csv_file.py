"""With Jinja2 we are able to work with CSV files as well. Let's write some code with CSV
and see how does it work."""

import jinja2
import csv

csv_file = "jinja2_csv_file.csv"
with open(csv_file) as csv_file:
    read_csv = csv.DictReader(csv_file)
    for elements in read_csv:
        bgp_neighbors = elements["bgp_neighbor"]
        bgp_neighbors = bgp_neighbors.split()
        elements["bgp_neighbor"] = bgp_neighbors
        template_file = "jinja2_conditionals.j2"
        with open(template_file) as reader:
            bgp_template = reader.read()
        bgp_template = jinja2.Template(bgp_template)
        output = bgp_template.render(elements)
        print(output)