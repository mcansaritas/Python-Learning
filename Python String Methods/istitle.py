"""The istitle() method returns True if all words in a text start with a upper case letter,
AND the rest of the word are lower case, otherwise False. Symbols and numbers are ignored.
The syntax is string.istitle()."""

our_text = "Hello, And Welcome To My World!"  # This is our string to check
title_check = our_text.istitle()  # This will check for title
print(title_check)  # Tjis will return True

print('-'*30)

a = "HELLO, AND WELCOME TO MY WORLD"  # This is our string to check
b = "Hello"  # This is our string to check
c = "22 Names"  # This is our string to check
d = "This Is %'!?"  # This is our string to check

print(a.istitle())  # This will print out False, all characters are upper case
print(b.istitle())  # This will print out True
print(c.istitle())  # This will print out True
print(d.istitle())  # This will print out True
