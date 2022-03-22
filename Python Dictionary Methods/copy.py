"""The copy() method returns a copy of the specified dictionary. The syntax is
dictionary.copy()."""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # This is our dictionary 

print(car)  # This will print out our dictionary

print('-'*30)

copied_dictionary = car.copy()  # This will copy our dictionary to another one
print(copied_dictionary)  # This will print out copied cell

# We can see that our dicitonaries are the same. Let's check is ID in memory

print(id(copied_dictionary))  # This is the memory place for copied dictionary
print(id(car))  # This is the memory place for original dictionary

# We can see that they are not the same in memory.
