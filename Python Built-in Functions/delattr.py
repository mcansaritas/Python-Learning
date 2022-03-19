"""The built-in delattr() method will delete the specified attribute from the specified object
The syntax how we can write it is delattr(object, attribute)."""

class Person:
    name = "Mertcan"
    age = 27
    country = "Turkey"

print(Person.age)  # We can see that the age attribute is written as 27
delattr(Person, "age")
print(Person.age)  # Right now there is no attribute named 'age'
