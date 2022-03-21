"""The isalnum() method returns True if all the characters are alphanumerical, meaning alphabet
letter (a-z) and numerical numbers (0-9).Example of characters that are not alphanumeric:
(space)!#%&? etc. The syntax is string.isalnum()."""

our_text = "company123"  # This is our initial text to check alphanumerical characters
checking_alphanumeric = our_text.isalnum()  # This will check the string
print(checking_alphanumeric)  # This will return True

print('-'*30)

our_text1 = "Company 12"
checking_alphanumeric = our_text1.isalnum()
print(checking_alphanumeric)  # This will return False because of whitespace
