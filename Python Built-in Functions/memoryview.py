"""The built-in memoryview() method returns a memory view object from a specified object. The syntax
is memoryview(obj)."""

x = memoryview(b"Hello")
print(x)

print(x[0])  # It returns the Unicode of the first character
print(x[1])  # It returns the Unicode of the second character
