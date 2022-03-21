"""The islower() method returns True if all the characters are in lower case, otherwise False.
Numbers, symbols and spaces are not checked, only alphabet characters. The syntax is 
string.islower()."""

our_text = "hello world!"  # This is our string to check
lower_case_checking = our_text.islower()  # This will check alphabet characters for lower case
print(lower_case_checking)  # This will print True

print('-'*30)

a = "Hello world!"  # This is our string to check for lower case
b = "hello 123"  # This is our string to check for lower case
c = "mynameisPeter"  # This is our string to check for lower case

print(a.islower())  # This will print out False
print(b.islower())  # This will print out True
print(c.islower())  # This will print out False
