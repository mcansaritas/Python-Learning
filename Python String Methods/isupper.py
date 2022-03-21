"""The isupper() method returns True if all the characters are in upper case, otherwise False.
Numbers, symbols and spaces are not checked, only alphabet characters. The syntax is
string.isupper()."""

our_text = 'THIS IS NOW TESTING FOR UPPER'  # This is our string to check
upper_checking = our_text.isupper()  # This will check is all characters are upper"
print(upper_checking)  # This will print True

print('-'*30)

a = "Hello World!"  # This is our string to check
b = "hello 123"  # This is our string to check
c = "MY NAME IS PETER"  # This is our string to check

print(a.isupper())  # This will print out False
print(b.isupper())  # This will print out False
print(c.isupper())  # This will print out True
