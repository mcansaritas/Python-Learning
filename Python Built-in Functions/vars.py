"""The built-in vars() method returns the __dic__ attribute of an object. The __dic__ attribute
is a dictionary containing the object's changeable attributes. The syntax is vars(object)."""

class Person:
    name = "John"
    age = 36
    country = "norway"

x = vars(Person)  # This are the changeable attributes of class Person
print(x)  # This prints out all attributes that we can change
