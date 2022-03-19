"""The built-in iter() method returns an iterable object. The syntax is iter(object, sentinel).
Object is required, and sentinel is optional."""

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

# It works like for loop in order to print all elements in the list
