"""We have an update method for dictionaries and it combines to dictionary together. When 
combining it can change the value of a key, and add unique key and value pairs."""

dictionary  = {"system_ip": "1.1.1.1", "release": "22.2R1", "chassis": "7750-SR"}  # This is our list

print(dictionary)  # We printed before combining with other dictionary

update = {"chassis": "7950-XRS", "bof_ip": "10.10.10.1"}

print(update)  # This is the dictionary that we are going to update
print(dictionary.update(update))  # It returns None but updates the dictionary
print(dictionary)  # This prints out the updated library
