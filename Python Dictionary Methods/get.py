"""The get() method returns the value of the item with the specified key. The syntax is 
dictionary.get(keyname, value)."""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}  # This is our dictionary

model_value = car.get("model")  # This will get the value of the key named 'model'
print(model_value)

# Also, we have a chance to specify a return value. Default return value is none

specified_return = car.get('price', 12345)  # This is trying to get a value of non-existince key
print(specified_return)  # This will return our specified value 12345
print(car)  # This will print out our dictionary
