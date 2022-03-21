"""The partition() method searches for a specified string, and splits into a tuple containing
three elements. The first element contains the part before the specified string. The second
element contains the specified string. The third element contains the part after the string.
This method searches for the first occurrence of the specified string. The syntax is
string.partition(value)."""

our_text = "I could eat bananas all day"  # This is our text
partition_text = our_text.partition("bananas")  # This will search 'bananas' and return a tuple
print(partition_text)  # The tuple is printed out

print('-'*30)

our_text = "I could eat bananas all day"  # This is our text
partition_text = our_text.partition("apples")  # This will search 'apples' and return a tuple
print(partition_text)  # This will print out a tuple
