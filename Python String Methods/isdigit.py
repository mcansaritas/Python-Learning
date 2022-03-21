"""The isdigit() method returns True if all the characters are digits, otherwise return False.
Exponents are also considered to be a digit. The syntax is string.isdigit()."""

our_text = "50800"  # This is string that we want to check
string_digit = our_text.isdigit()  # This is digit checking for the string
print(string_digit)  # This will print out True

print("-"*30)

a = "\u0030"  # This is unicode for 0
b = "\u00B2"  # This is unicode for ²

print(a.isdigit())  # This will print out True
print(b.isdigit())  # This will print out True
