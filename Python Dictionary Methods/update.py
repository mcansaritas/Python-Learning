"""The update() method inserts the specified items to the dictionary. The specified items can
be a dicitonary, or an iterable object with the key value pairs. The syntax is dictionary.update(iterable)."""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # This is our dictionary

car.update({"color": "White"})  # This will insert a new key-value pair
print(car)
