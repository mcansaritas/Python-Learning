"""The ljust() method will left align the string, using the specified character (space is
default) as the fill character. The syntax is string.ljust(length, character)."""

our_text = 'Banana'  # This is our text for left aligning
left_aligned = our_text.ljust(20)  # This will left align our text
print(left_aligned, 'is my favourite fruit')  # This will print out left aligned string

print('-'*30)

our_text1 = "banana"  # This is our text for left aligning
left_aligned = our_text1.ljust(20, "O")  # This will left alig our text
print(left_aligned)  #This will print out left aligned string
