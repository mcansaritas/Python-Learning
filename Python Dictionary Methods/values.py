"""The values() method returns a view object. The view object contains the values of the dictionary,
as a list. The view object will reflect any changes done to the dictionary. The syntax is 
dictionary.values()."""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # This is our dictionary

x = car.values()  # This will get the values from the dictionary
print(x)  # This will print out all values in dictionary as a list

# When a values is changed in the dictionary, the view object also gets updated

car['year'] = 2012  # We updated the key's value named 'year' to 2012
print(x)  # This will print out new values
