"""The isalpha() returns True if all the characters are alphabet letters (a-z). Example of
characters that are not alphabet letters : (space)!#%&? etc."""

our_text1 = "Company"  # This is our string to check
alphabet_checking = our_text1.isalpha()  # This will check our string
print(alphabet_checking)  # This will return True

print('-'*30)

our_text2 = 'Company Ford'  # This is our string to check
alphabet_checking = our_text2.isalpha()  # This will check our string
print(alphabet_checking)  # This will return False
