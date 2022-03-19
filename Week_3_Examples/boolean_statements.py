"""Python has its own Boolean statements. We can do boolean and, or, and not operation. Let's
write some code and see how does it work."""

a = True
b = False

print(a and b)  #This is and operation with boolean, True and False, it is False
print(a and (not b))  # This is and operation with boolean, True and True is it True
print(10 < 2)  # It is a statement as 10 is smaller than 2 and it is False

print("-"*30)

print(a or b)  # This is or operation with boolean, True or False, it is True
print((not a) and b)  # This is or operation with boolean, False or False, it is False
print((10 > 2) or (10 > 11))  # This is True and False, so it is False

print("-"*30)
