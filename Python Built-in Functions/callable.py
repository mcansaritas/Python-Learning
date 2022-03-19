"""The built-in callable() method returns True if the specified object is callable, otherwise
it returns False. You only need to specify the name of the object you want to check."""

def x():
    a = 5

call = callable(x)
print(call)  # This will return True, because x is a function

"""A normal variable is not callable."""

print("-"*30)

y = 5

call = callable(y)
print(call)  # This will return False, because y is a variable
