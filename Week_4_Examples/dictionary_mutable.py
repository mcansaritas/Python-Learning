"""Dictionary is a mutable data type. That means it allow changes in the values. Let's
run some code and what we can do with that."""

dictionary  = {"system_ip": "1.1.1.1", "release": "22.2R1", "chassis": "7750-SR"}  # This is our list
print(dictionary)  # This will print our dictionary

copied_dictionary = dictionary.copy()  # This will copy our dictionary to another variable
print(copied_dictionary)  # This will print our copied cell
print(id(dictionary))  # This will print our original dictionary's memory place
print(id(copied_dictionary))  # This will print our copied dictionary's memory place
print(dictionary is copied_dictionary)  # We can see that they are not in the same place and it is False

print("-"*30)

print(dictionary)  # This will print our dictionary before pop
print(dictionary.pop("chassis"))  # Then we remove the key named "chassis" and it returns its value
print(dictionary)  # Then we printed the dictionary after removal