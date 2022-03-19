"""The built-in id() method returns a unique ID for the specified object. All objects in Python
has its own unique ID. The ID is assigned to the object when it is created. The ID is the object's
memory address, and will be different for each time you run the program. The syntax is id(object)."""

x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)

# It shows use where the variable x is located in the memory