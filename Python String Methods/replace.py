"""The replace() method replaces a specified phrase with another specified phrase. All occurences
of the specified phrase will be replaced, if nothing else is specified. The syntax is
string.replace(oldvalue, newvalue, count)"""

our_text = 'I like bananas'  # This is our text
replaced_text = our_text.replace('bananas', 'apples')  # This will replace 'bananas' with 'apples'
print(replaced_text)  # This will print out the replaced text

print('-'*30)

our_text = "one one was a race horse, two two was one too."  # This is our text
replaced_text = our_text.replace("one", "three")  # This will replace 'one' with 'three'
print(replaced_text)

print('-'*30)

our_text = "one one was a race horse, two two was one too."  # This is our text
replaced_text = our_text.replace("one", "three", 2)  # This will replace 'one' with 'three' 2 times
print(replaced_text)  # This will print out the replaced text
