"""The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: { }. The format() method returns the formatted
string. The syntax is string.format(value1, value2...)"""

our_text = 'This is our testing to understand how {method} is working.'  # This is initial string
new_text = our_text.format(method = "format()")  # This is how formatting is done
print(new_text)  # This will print out the formatted text

print('-'*30)

our_text1 = "My name is {fname}, I'm {age}".format(fname = "Mertcan", age = 27)
our_text2 = "My name is {0}, I'm {1}".format("Mertcan",27)
our_text3 = "My name is {}, I'm {}".format("Mertcan", 27)

print(our_text1)
print(our_text2)
print(our_text3)
