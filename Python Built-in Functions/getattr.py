"""The built-in getattr() method returns the value of the specified attribute from the specified
object. The syntax is getattr(object, attribute, default)."""

class Person:
    name = "Mertcan"
    age = 27
    country = "Turkey"

x = getattr(Person, 'age')
y = getattr(Person, 'country')

print("The age of the person is %d, and country is %s" % (x, y))