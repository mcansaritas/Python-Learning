"""The items() method returns a view object. The view object contains the key-value pairs of
the dictionary, as tuples in a list. The view object will reflect any changes done to the
dictionary. The syntax is dictionary.items()."""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # This is our dictionary

dict_items = car.items()  # This will get us a tuple key-value pairs
print(dict_items)  # This will print out the tuple

# When an item in the dictionary changes value, the view object also gets updated

car['year'] = 2012  # This 'year' key's value is changed to 2012
print(dict_items)  # We can see that our tuple is changed as well
