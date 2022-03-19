"""In Python string, integer, list, float, tuple and dictionarie can be used with Boolean.
A value will be false, and other will be True. Let's test this and learn which ones are True
or False. Also Python has a special data type called None. It is a statement boolean False."""

a = "String"  # This is a string. Strings are boolean True
b = ""  # This is an empty string. Empty strings are boolean False

print(bool(a))  # True
print(bool(b))  # False

print("-"*30)

c = 0  # This is integer 0. Integer 0 means boolean False
d = 200  # This is integer 200. Integers are boolean True
e = -200  # This is integer -200. Negative integers are also boolean True

print(bool(c))  # False
print(bool(d))  # True
print(bool(e))  # True

print("-"*30)

f = []  # This is an empty list, and it means boolean False
g = [1, 2, "anywthing"]  # This is a list, and it means boolean True.

print(bool(f))  # False
print(bool(g))  # True

print("-"*30)

h = {}  # This is an empty dictionary, and it means boolean False
i = {"key": "value"}  # This is a dictionary, and it means boolean True

print(bool(h))  # False
print(bool(i))  # True

print("-"*30)

my_none_value = None  # This is a data type None
print(type(my_none_value))  # It will print None
print(bool(my_none_value))  # It will print False