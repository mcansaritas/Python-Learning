"""Dictionary is a mapping between a key and value. They are not sequential. They are created
with {}. Let's write some examples with line of code."""

dictionary = {}  # This is an empty dictionary.
print(type(dictionary))  # This will print class dictionary

print("-"*30)

dictionary ["element1"] = "1.1.1.1"  # This will assign a key and its value and add to dictionary.
dictionary ["element2"] = "2.2.2.2"  # This will assign a key and its value and add to dictionary.
vendor = "Vendor"  # We have a variable and we bind it to a string.
dictionary [vendor] = "Nokia"  # This will assign a key and its value and add to dictionary
dictionary ["OS"] = "SROS"  # This will assign a key and its value and add to dictionary
print(dictionary)  # This will print my dictionary with new key/value pairs

print("-"*30)

## If we want to see a key's value, we need to use [] and inside the key name. It is key sensitive.

print(dictionary["Vendor"])  # This will print the value of key "vendor"
print(dictionary["element1"])  # This will print the value of key "vendor"
print(dictionary["OS"])  # This will print the value of key "vendor"