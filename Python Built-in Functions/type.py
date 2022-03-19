"""The built-in type() method returns the type of the specified object. The syntax is
type(object, bases, dict). The object is required and bases and dict is optional. Bases
specifies the base classes, and dict specifies the namespaces with the definition of the class."""

a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

print(x)  # This prints out the type tuple
print(y)  # This prints out the type string
print(z)  # This prints out the type integer
