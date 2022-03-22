"""The pop() method removes the specified item from the dictionary. The value of the removed
item is the return value of the pop() method. The syntax is dictionary.pop(keyname, defaultvalue)."""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # This is our dictionary

car.pop("model")  # This will pop the key named 'model' and return the value of 'model'
print(car)  # This will print out the updated dictionary

# In order to see the return value of pop method, we can assign to a variable

x = car.pop('year')  # This will pop from the dictionary key named 'year'
print(x)  # This will print out the value of the pop method
