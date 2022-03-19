"""The built-in isinstance() method returns True if the specified object is of the specified type
, otherwise returns False. The syntax is isinstance(object, type)."""

x = isinstance(5, int)
print(x)  # It returns True, because 5 is an integer

print("-"*30)

y = isinstance("Hello", (float, int, str, list, dict, tuple))
print(y)  # It returns True, because 'Hello' is a string and str is the types

print("-"*30)

my_tuple = (1, 2, 3)
z = isinstance(my_tuple, str)
print(z)  # It returns False, because our variable is not a string

print("-"*30)

tuple1 = ("Mertcan", 1, "Saritas")
a = isinstance(tuple1, tuple)
print(a)  # It returns True, because our variable is a tuple
