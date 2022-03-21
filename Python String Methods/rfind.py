"""The rfind() method finds the last occurence of the specified value. The rfind() method returns
-1 if the value is not found. The rfind() method is almost the same as he rindex() method. The
syntax is string.rfind(value, start, end)."""

our_text = "Mi casa, su casa."  # This is our text
x = our_text.rfind("casa")  # This will search for 'casa
print(x)  # This will print out the index of the 'casa'

print('-'*30)

our_text = "Hello, welcome to my world."  # This is our text
x = our_text.rfind("e")  # This will search for 'e'
print(x) # This will print out the index of the last 'e'

print('-'*30)

our_text = "Hello, welcome to my world."  #This is our text
x = our_text.rfind("e", 5, 10)  # This will search for 'e' between the position 5 and 10
print(x)  # This will print out the index of the last 'e' between the position 5 and 10

print('-'*30)

our_text = "Hello, welcome to my world."  # This is our text

print(our_text.rfind("q"))  # When the value is not found, the method returns -1
print(our_text.rindex("q"))  # When the value is not found, the method raises and exception
