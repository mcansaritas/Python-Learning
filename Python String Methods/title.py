"""The title() method returns a string where the first character in every word is upper case.
Like a header, or a title. If the word contains a number or a symbol, the first letter after
that will be converted to upper case. The syntax is string.title()."""

our_text = 'Welcome to my world.'  # This is our text to convert
title_convert = our_text.title()  # This will convert the text into title
print(title_convert)  # This will print out the converted title

print('-'*30)

our_text = "Welcome to my 2nd world"  # This is our text to convert
title_convert = our_text.title()  # This will convert the text into title
print(title_convert)  # This will print out the converted title

print('-'*30)

our_text = "hello b2b2b2 and 3g3g3g"  # This is our text to convert
title_convert = our_text.title()  # This will convert the text into title
print(title_convert)  # This will print out the converted title
