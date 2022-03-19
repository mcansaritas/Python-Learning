"""The built-in ascii() method returns a readable version of any object. The ascii() method will
replace any non-ascii characters with escape character."""

print(("My name is Ståle"))  # This is before ascii fix
x = ascii("My name is Ståle")  # This is after ascii fix
print(x)

"""In this example, å will be replaced with \xe5. It is not an ascii character. It will be written
with escape character '\'."""