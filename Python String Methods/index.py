"""The index() method finds the first occurence of the specified value. The index() method raises
an exception if the value is not found. The index() method is almost the same as the find() method
the only difference is that the find() method returns -1 if the value is not found. The syntax
is string.index(value, start, end)."""

our_text = "This is our testing for index() method to understand how it works."  # This is our string
index_value = our_text.index("index()")  # This will search for word 'index()' in the string
print(index_value)  # This will print out the index value

print('-'*30)

our_text1 = "Hello, welcome to my world."  # This is our second string
index_e = our_text1.index("e")  # We will search in the string for letter 'e'
print(index_e)
