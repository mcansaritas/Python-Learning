"""The isdecimal() method returns True if all the characters are decimals (0-9). This method
is used on unicode objects.The syntax is string.isdecimal()."""

our_text = '\u0033' # This is unicode for 3
decimal_checking = our_text.isdecimal()
print(decimal_checking)

print('-'*30)

a = "\u0030"  # This is unicode for 0
b = "\u0047"  # This is unicode for G

print(a.isdecimal())  # This will print out True
print(b.isdecimal())  # This will print out False
