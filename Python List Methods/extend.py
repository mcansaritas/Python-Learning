"""The extend() method adds the specified list elements (for any iterable) to the end of the
current list. The syntax is list.extend(iterable)."""

fruits = ['apple', 'banana', 'cherry']  # This is our list named 'fruits'
cars = ['Ford', 'BMW', 'Volvo']  # This is our list named 'cars'

fruits.extend(cars)  # This will add cars into fruits list
cars.extend(fruits)  # This will add fruits into cars list (Keep in mind fruits list is updated)

print(fruits)  # This will print out new 'fruits' list
print(cars)  # This will print out new 'cars' list