"""There are some string methods that we can use in Python. Let's test it with the line of code.
And see what is the output and what is expected."""

string = "    There is snow here \n\n"
print(string)

"""We can see that there are some whitespace at the beginning and at the end there are 2 enters.
With strip method, we are able to remove these whitespaces and enters.Let's try this one out."""

print(string.strip())  # We can see that it is stripped from both end and beginning.
print(string.rstrip())  # This removes trailing whitespaces of the string.
print(string.lstrip())  # This removes leading whitespaces of the string.
