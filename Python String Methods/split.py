"""The split() method splits a string into a list. You can speicfy the separator, default separator
is any whitespace. When the maxsplit is specified, the list will contain the specified number of
elements plus one. The syntax is string.split(separator, maxsplit)."""

our_text = "welcome to the jungle"  # This is our text to split into
split_text = our_text.split()  #This will split our text based on whitespaces
print(split_text)

print('-'*30)

our_text = "hello, my name is Peter, I am 26 years old"  # This is our text to split into
split_text = our_text.split(", ")  # This will split based on comman
print(split_text)

print('-'*30)

our_text = "apple#banana#cherry#orange"  # This is our text to split into
split_text = our_text.split("#")
print(split_text)

print('-'*30)

our_text = "apple#banana#cherry#orange" # setting the maxsplit parameter to 1, will return a list with 2 elements!
split_text = our_text.split("#", 1)
print(split_text)
