"""The built-in setattr() method sets the value of the specified attribute of the specified
object. The syntax is setattr(object, attribute, value). All of the parameters are required
in this method."""

class Person:
    name = "John"
    age = 36
    country = "Norway"

setattr(Person, 'age', 40)  # This will change the attribute age to 40
x = getattr(Person, "age")  # We will assign the age value to x
print(x)  # We will print out x which is 40
