"""The built-in dir() method returns all properties and methods of the specified object, without
any the values. This method will return all the properties and methods, even built-in properties
which are default for all objects. The syntax is dir(object)"""

class Person:
    name = "Mertcan"
    age = 27
    country = "Turkey"

print(dir(Person))

# In the output we can see that built-in methods as well as properties