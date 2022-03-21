"""The isidentifier() method returns True if the string is a valid identifier, otherwise False.
A string is considered a valid identifier if it only contains alphanuerical letters (a-z) and
(0-9), or underscores (_). A valid identifier cannot start with a number, or contain any space.
The syntax is string.isidentifier()."""

our_text = "Demo"  # This is our string to check if a valid identifier
identifier_checking = our_text.isidentifier()  # This will check the string for a valid identifier
print(identifier_checking)  # This will print out True

print('-'*30)

a = "MyFolder"  # This is our string to check if a valid identifier
b = "Demo002"  # This is our string to check if a valid identifier
c = "2bring"  # This is our string to check if a valid identifier
d = "my demo"  # This is our string to check if a valid identifier

print(a.isidentifier())  # This will print out True
print(b.isidentifier())  # This will print out True
print(c.isidentifier())  # This will print out False because it starts with number
print(d.isidentifier())  # This will print out False because of whitespaces
