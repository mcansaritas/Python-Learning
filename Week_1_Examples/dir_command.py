"""With dir command we are able to see all attributes and methods that we can use for objects
in our code. We are creating string, integer and list. Let's see what will be the output."""

my_string = "String"
my_integer = 10
my_list = (1, 2, 3)

print(dir())  # It shows attributes in our line of code.

print("-"*30)

print(dir(my_string))  # It shows methods that we can use with a string.
print(my_string.upper())  # It prints with all upper case.
print(my_string.lower())  # It prints with all lower case.
print(my_string.index("S"))  # It shows what is the index of "S"

"""When we run the command, we can see our variables my_string, my_integer, and my_list."""