"""The built-in bytes() method returns a bytes object. It can convert objects into bytes objects,
or create empty bytes objects of the specified size. The difference between bytes() and bytesarray()
is that bytes() return an object that cannot be modified, and bytearray() returns an object that
can be modified. The syntax how we can writes bytes() method is bytes(x, encoding, error). X is a source to use
when creating bytes object. If a string is used, then we need encoding, and error that specifies
what to do if the encoding fails."""

"""When an integer is used, it is the size of the bytes."""

x = bytes(4)
print(x)  # This will print 4 times hexadecimal 00

print("-"*30)

string = "Welcome"
array = bytes(string, 'utf-8')  # This will print a string with UTF-8 encoding
print(array)
