"""The casefold() method returns a string where all the characters are lower case. This method
is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning
that it will convert more characters into lower case, and will find more matches when comparing
two strings and both are converted using the casefold() method. The syntax is string.casefold()."""

our_text = 'This is testing how casefold() method is working.'  # This is our string
print(our_text)  # This will print out our initial string

print('-'*30)

casefold_method = our_text.casefold()  # This will convert our string to lower case
print(casefold_method)  # This will print out our new string
