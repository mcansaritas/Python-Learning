"""The endswitch() method returns True if the string ending with the specified value, otherwise
it returns False. The syntax is string.endswitch(value, start, end). The value is mandatory, and
the other parameters are optional."""

our_text = 'This is our testing how endswitch() method is working.'  # This is our initial text
print(our_text)  # This will print out our initial string

ending_check = our_text.endswith('.')
print(ending_check) # This will print out if ending is our desired character or not
