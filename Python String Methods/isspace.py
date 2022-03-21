"""The isspace() method returns True if all characters in a string are whitespaces, otherwise
False. The syntax is string.isspace()."""

our_string = "   "  # This is our string with all whitespaces
space_check = our_string.isspace()  # This will check against whitespaces
print(space_check)  # This will print True

print('-'*30)

our_string = "   s   "  # This is our string with a alphabet character
space_check = our_string.isspace()  # This will check against whitespaces
print(space_check)  # This will print False
