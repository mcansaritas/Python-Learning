"""The isnumerical() method returns True if all characters are numeric (0-9), otherwise False.
Exponents, like ² and ¾ are also considered to be numeric values."-1" and "1.5" are not considered
numeric values, because all the characters in the string must be numeric, and the - and . are not."""

our_text = "5442424"  # This is our string to check
numerical_check = our_text.isnumeric()  # This will check for numeric values
print(numerical_check)  # This will print out True

print('-'*30)

a = "\u0030"  #This is unicode for 0
b = "\u00B2"  #This is unicode for &sup2 exponential 2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())  # This will print out True
print(b.isnumeric())  # This will print out True
print(c.isnumeric())  # This will print out False
print(d.isnumeric())  # This will print out False
print(e.isnumeric())  # This will print out False
