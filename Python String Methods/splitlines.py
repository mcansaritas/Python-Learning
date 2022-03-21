"""The splitlines() method splits a string into a list. The splitting is done at line breaks.
The syntax is string.splitlines(keeplinebreaks)."""

our_text = """Thank you for the coding. 
Welcome to coding world.
"""  # This is our multiline text

splitted_lines = our_text.splitlines()  # This will split the text
print(splitted_lines)  # This will print out splitted lines

print('-'*30)

our_text = "Thank you for the music\nWelcome to the jungle"  # This is our multiline text
splitted_lines = our_text.splitlines(True)  # This will keep line breaks
print(splitted_lines)   # This will print out the splitted lines with breaks
