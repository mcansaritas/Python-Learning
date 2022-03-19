"""This built-in bytearray() method returns a bytearray object. It can revert objects into byte
array objects, or create an empty bytearray object of the specified size. The syntax of bytearray
is bytearray(x, encoding, error). X is the source to use when creating bytearray. Encoding is the
encoding of the string. Error specifies what to do if the encoding fails."""

"""If a string, must provide encoding and errors parameters, bytearray converts the string to
bytes using str.encode()."""

string = "Mertcan"
array1 = bytearray(string, 'utf-8')
array2 = bytearray(string, 'utf-16')
print(array1)
print(array2)

print("-"*30)

"""If an integer, it creates an array of that size and initialized with null bytes"""

x = bytearray(4)
print(x)

print("-"*30)

"""If an object, read-only buffer will be used to initialize the bytes array."""

array1 = bytearray(b"abcd")
for value in array1:
    print(value)

array2 = bytearray(b"aaaacccc")
print("Count of c is:", array2.count(b"c"))

print("-"*30)

"""If an iterable in range 0-256, used as the initial contents of an array."""

list = [1, 2, 3, 4]
array = bytearray(list)
print(array)
print("Count of bytes:", len(array))

print("-"*30)

"""If no source, then an array of size 0 is created."""

array = bytearray()
print(array)
