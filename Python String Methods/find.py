"""The find() method finds the first occurance of the specified value. The find() method returns
-1 if the value is not found. The find() method is almost the same as the index() method, the
only difference is that the indeX() method raises an exception if the value is not found. The
syntax is string.find(value, start, end). Value is mandatory and other parameters are optional."""

our_text = "This is testing how find() method is working."  # This is our initial text
finding_find = our_text.find('find')  # This will search for first occurence 'find'
print(finding_find)  # This will print out the index of the 'find' string

print('-'*30)

finding_e = our_text.find('e') # This will search for first occurence 'e' in the string
print(finding_e) # This will print out the index of the 'e' string

print('-'*30)

find_not_included = our_text.find('q')
index_not_included = our_text.index('q')

print(find_not_included) # This will print out the index of the 'q' and returns -1
print(index_not_included) # This will print out the index of the 'q' and raise an exception
