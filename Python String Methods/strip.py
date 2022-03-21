"""The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end)
characters (space is the default leading character to remove). The syntax is string.strip(characters)."""

our_text = "     banana     "  # This is our string to check
strip_space = our_text.strip()  # This will removes any leading and trailing whitespaces
print("of all fruits", strip_space, "is my favorite")  # This will print out the text

print('-'*30)

our_text = ",,,,,rrttgg.....banana....rrr"   # This is our string to check
strip_characters = our_text.strip(",.grt")  # This will removes any leading and trailing whitespaces
print(strip_characters)  # This will print out the string
