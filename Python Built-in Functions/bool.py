"""The bool() function returns the boolean value of a specified object. The object will always
return True, unless the object is empty, the object is False, the object is 0, and the object is
None."""

x = bool(1)
y = bool(())
z = bool({})

print(x)  # This will return True, because our integer is not 0
print(y)  # This will return False, because our tuple is empty
print(z)  # This will return False, because our dictionary is empty
