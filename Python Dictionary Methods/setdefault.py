"""The setdefault() method returns the value of the item with the specified key. If the key does
not exist, insert the key, with the specified value. In syntax is dictionary.setdefault(keyname, value).
If the key exist, this has not effect. If the key does not exist, this value becomes the key's value."""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # This is our dictionary

x = car.setdefault("model", "Bronco")  # We are binding a default value to key named 'model'
print(x)  # This will print out the value of 'model' which is 'Mustang'

# There is no key value named 'color'. Item does not exist, insert 'color' with the value 'white'

x = car.setdefault("color", "white")
print(x)
print(car)
