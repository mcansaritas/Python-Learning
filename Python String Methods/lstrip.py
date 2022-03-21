"""The lstrip() method removes any leading characters (space is the default leading character
to remove). The syntax is string.lstrip(characters)."""

our_text = "     banana     "  # This is our string to test
strip_space = our_text.lstrip()  # This will remove all leading whitespaces
print("Of all fruits", strip_space, "is my favorite")  # This text eill be printed out

print('-'*30)

our_text1 = ",,,,,ssaaww.....banana"   # This is our string to check
lead_strip = our_text1.lstrip(",.asw")  #This will remove leading characters
print(lead_strip)  # This will print out string with removed characters

