"""The popitem() method removes the item that was last inserted into the dictionary. In version
before 3.7, the popitem() method removes a random item. The removed item is the return value of
the popitem() method, as a tuple. The syntax is dictionary.popitem()"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # This is our dictionary

car.popitem()  # This will remove the last item from dictionary which is 'year'
print(car)

# In order to see which items are removed, then we can bind it to a variable

x = car.popitem() # This will pop the last item which is 'model'
print(x)  # This will return a tuple of the removed element
