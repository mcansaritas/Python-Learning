"""The built-in issubclass() method returns True if the specified object is a subclass of the
specified object, otherwise return False. The syntax is issubclass(object, subclass)."""

class myAge:
    age = 36

class myObj(myAge):
    name = "John"
    age = myAge

x = issubclass(myObj, myAge)
print(x)  # It returns True, because myObj is a subclass of the myAge