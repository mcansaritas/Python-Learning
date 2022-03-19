"""Let's work on Python 'for' loops first. It needs to follow Python naming convention.
If the container is empty, then the code block never be exectured. With enumerate we can
see index and its value."""

my_list = ["1.1.1.1", "2.2.2.2", "3.3.3.3"]
print(my_list)  # This will print our whole list

for loop in my_list :  # Loop is a variable for 'for' loops
    print("My IP address is {}".format(loop))  # This will print our statement
    print(loop)  # This will print the element in the list

print("-"*30)

for loop in enumerate(my_list):  # We are using enumerate method and it returns index and value.
    print(loop)  # This will print a tuple with 2 elements

print("-"*30)

for index, element in enumerate(my_list):  # Index is assigned to index and element to element
    print(index, element)  # This will print their values

print("-"*30)

variable1, variable2 = [1, "anything"]
print(variable1, variable2)

print("-"*30)