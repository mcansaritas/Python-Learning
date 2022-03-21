"""The sort() method sorts the list ascending by default. You can also make a function to decide
the sorthing criteria(s). The syntax is list.sort(reverse=True|False, key=myFunc). The reverse
is optional and default is False and ascending order, if True it is descending order. Key is
optional and it is a function to specify the sorting criteria(s)."""

cars = ['Ford', 'BMW', 'Volvo']
print(cars)  # This will print out the original list of cars

print('-'*30)

cars.sort()  # This will sort the list in ascending order
print(cars)  # This will print out the updated list
