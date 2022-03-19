"""This method any() checks if any of the items in the list are True. This method will return
True if any item in the iterables are True, otherwise it will return False. In the iterable
object is empty, the any() function will return False."""

mytuple = (0, 1, False)  # This is my tuple.
x = any(mytuple)
print(x)  # This will return True, because we have elements which is True

print("-"*30)

myset = {0, 1, 0}  # This is my set
x = any(myset)
print(x) # This will return True, because we have elements which is True

print("-"*30)

mydict = {0 : "Apple", 1 : "Orange"}  # This is my dictionary
x = any(mydict)
print(x) # This will return True, because we have elements which is True

print("-"*30)

# When used on a dictionary, the any() function checks if any of the keys are True, not values.
