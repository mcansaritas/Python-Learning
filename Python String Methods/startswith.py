"""The startswith() method returns True if the string starts with the specified value, otherwise False.
The syntax is string.startswith(value, start, end)."""

our_text = "Hello, welcome to my world."  # This is our string to check
start_checking = our_text.startswith("Hello")  # This will check if text starts with 'Hello'
print(start_checking)  # This will print out True

print('-'*30)

our_text = "Hello, welcome to my world."  # This is our string to check
start_checking = our_text.startswith("wel", 7, 20)  # This will check position 7 to 20 and starts with 'wel'
print(start_checking)  # This will print out True
