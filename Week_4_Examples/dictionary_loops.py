"""We can use loop for dictionaries as well. Let's write some line of codes and see how does
it work and what we can do it that."""

dictionary  = {"system_ip": "1.1.1.1", "release": "22.2R1", "chassis": "7750-SR"}  # This is our list

for keys in dictionary:  # This is a 'for' loop to return keys in the dictionary
    print(keys)

print("-"*30)

for values in dictionary.values():  # This is a 'for' loop to return values in the dictionary
    print(values)

print("-"*30)

for tuple in dictionary.items():
    print(tuple)

print("-"*30)

for key, value in dictionary.items():
    print(key)
    print(value)

print("-"*30)