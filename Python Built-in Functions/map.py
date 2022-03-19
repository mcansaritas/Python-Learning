"""The built-in map() method executes a specified function for each item in an iterable. The
item is sent to the function as a parameter. The syntax is map(function, iterables). Function is
required, because it is the function we want to execute. Iterable is required, it can be an
iterator, sequence, or collection object. You can send many iterables as you like, just make sure
the function has one parameter for each iterable."""

def my_function(x):
    return len(x)

x = map(my_function, ("orange", "apple", "cherry"))
print(list(x))  # It put the variables inside the function and convert the output into a list