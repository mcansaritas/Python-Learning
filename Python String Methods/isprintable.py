"""The printable() method returns True if all the characters are printable, otherwise False.
Example of none printable character can be carriage return and line feed. The syntax is
string.isprintable()."""

our_text = 'Hello! Are you #1'  # This is our string to check
print_check = our_text.isprintable()  # This will check for printable characters
print(print_check)  # This will return True

print('-'*30)

our_text1 = "Hello!\nAre you #1?"  # This is our string with multiple lines
print_check = our_text1.isprintable()  # This will check for printable characters
print(print_check)  # This will return False
