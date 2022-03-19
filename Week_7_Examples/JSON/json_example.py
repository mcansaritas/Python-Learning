"""JSON is another serialization protocol. We are converting byte streams and send it. It is
very similar syntax from data structure point of view. Let's write some code and see what is
the outcome."""

import json

my_list = list(range(10))
my_list.append("Mertcan")
my_list.append("Saritas")

my_dictionary = {"key1": "value1"}
my_dictionary["key2"] = my_list
my_dictionary["key3"] = False

print(my_dictionary)  # This prints out the original dictionary
print(json.dumps(my_dictionary))  # This prints out the JSON output

with open("json_file.json", "w") as writer:
    json.dump(my_dictionary, writer, indent=4)

with open("json_file.json") as reader:
    json_data = json.load(reader)

print(json_data)