"""The fromkeys() method returns a dictionary with the specified keys and specified values.
The syntax is dict.fromkeys(keys, value)."""

x = ('key1', 'key2', 'key3')  # This is a tuple for keys
y = 0  # This is value for values

from_keys_dict = dict.fromkeys(x, y)  # This will create a dictionary
print(from_keys_dict)  # This will print out created dictionary

# This will change tuple and values into a dicionary. Specifying a value is not mandatory

print('-'*30)

x = ('key1', 'key2', 'key3')
from_keys_dict = dict.fromkeys(x)
print(from_keys_dict)
