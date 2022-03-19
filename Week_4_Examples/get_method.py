"""We learned that we can get a key's value. We will get an error. Another way to get a 
key's value get() method. But get method does not give an error, but it returns None."""

dictionary  = {"system_ip": "1.1.1.1", "release": "22.2R1", "chassis": "7750-SR"}

print(dictionary.get("system_ip"))  # This will print the key 'system_ip' value
print(dictionary.get("release"))   # This will print the key 'release' value
print(dictionary.get("chassis"))   # This will print the key 'chassis' value
#print(dictionary["interface"])    # This will print the key 'interface' value. It is comment because of NameError
print(dictionary.get("interface"))    # This will print the key 'interface' value
print(type(dictionary.get("interface")))  # This will print type None