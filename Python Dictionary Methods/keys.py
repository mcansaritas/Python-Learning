"""The keys() method returns a view object. The view object contains the keys of dictionary,
as a list. The view object will reflect any changes done to the dictionary. The syntax is
dictionary.keys()."""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # This is our dictionary

dict_keys = car.keys()  # This will get the keys in our dictionary
print(dict_keys)  # This will print out the keys

# When an item is added in the dictionary, the view object also gets updated

car['color'] = 'white'
print(dict_keys) # This will print out the updated dictionary keys
