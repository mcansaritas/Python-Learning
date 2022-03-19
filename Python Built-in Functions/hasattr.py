"""The built-in hassattr() function returns True if the specified object has the specified attribute
and otherwise it returns False."""

class Person:
    name = "Mertcan"
    age = 36
    country = "Turkey"

x = hasattr(Person, 'age')
y = hasattr(Person, 'car')

print(x)  # It returns True, because our class has age attribute
print(y)  # It returns False, because our class has no car attribute
