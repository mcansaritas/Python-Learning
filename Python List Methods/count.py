"""The count() method returns the number of elements with the specified value. The syntax is
list.count(value)."""

fruits = ['apple', 'banana', 'cherry']  # This is our list
count_cherry = fruits.count("cherry")  # This is how we can count 'cherry'
print(count_cherry)  # It prints the number of cherry in the list

# This count will count the number of cheery written in list 'fruits'.

fruits.append('cherry')  # We are going to append 'cherry' to the end of the list
print(fruits)  # We will print the updated list
count_cherry = fruits.count("cherry")  # This is how we can count 'cherry'
print(count_cherry)  # It prints the number of cherry in the list
