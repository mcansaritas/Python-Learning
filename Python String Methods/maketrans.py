"""The maketrans() method returns a mapping that can be used with the translate() method to
replace specified characters. The syntax is string.maketrans(x, y, z). Parameter x is required
 and others are optional."""
 
our_text = 'Hello Sam!'  # This is our text
my_table = our_text.maketrans('S', 'P')  # This will replace the 'S' with 'P'
print(our_text.translate(my_table))  # This will print out the translated string


print('-'*30)

our_text = "Hi Sam!"  #This is our text
x = "mSa"  # This is our characters that will be changed
y = "eJo"  # This is our characters that will change
mytable = our_text.maketrans(x, y)  # This will replace the values in our string
print(our_text.translate(mytable))  # This will print out the new string 

print('-'*30)

our_text = "Good night Sam!"  # This is our text
x = "mSa"  # This is our characters that will be changed
y = "eJo"  # This will our characters that will change
z = "odnght"  # This will be removed from the string
mytable = our_text.maketrans(x, y, z)  # This will remove and change some characters
print(our_text.translate(mytable))  # This will print out the changed string

print('-'*30)

our_text = "Good night Sam!"  # This is our string
x = "mSa"  # This is our characters that will be changed
y = "eJo"  # This will our characters that will change
z = "odnght"  # This characters will be changed from string
print(our_text.maketrans(x, y, z))  # This will print a dictionary describing replacements in Unicode
