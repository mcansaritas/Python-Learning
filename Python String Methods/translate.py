"""The translate() method returns a string where some specified characters are replaced
with the character described in a dictionary, or a mapping table. Use the maketrans()
method to create a mapping table. If a character is not specified in the dictionary
or table, the character will not be replaced. If you use a dictionary, you must use
ascii codes instead of character. The syntax is string.translate(table)"""

# We used a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}  # This is our dictinary to change characters
our_text = "Hello Sam!"  # This is our initial text
print(our_text.translate(mydict))  # This will print out the replaced string

print('-'*30)

our_text = "Hello Sam!"  # this is our initial text
mytable = our_text.maketrans("S", "P")  # This will create a dictionary for translate method
print(our_text.translate(mytable))  # This will print out the replaced text

print('-'*30)

our_text = "Hi Sam!"  # This is our initial text
x = "mSa"  # This is our characters that will be changed
y = "eJo"  # this is our characters that will replace
my_dictionary = our_text.maketrans(x, y)  # This will create a dictionary for translate method
print(our_text.translate(my_dictionary))  # This will print out replaced text

print('-'*30)

our_text = "Good night Sam!"  # This is our initial text
x = "mSa"  # This is our characters that will be changed
y = "eJo"  # This is our characters that will replace
z = "odnght"  # This is characters that will be removed
mytable = our_text.maketrans(x, y, z)  # This will create a dictionary
print(our_text.translate(mytable))  # This will print out the replaced text
