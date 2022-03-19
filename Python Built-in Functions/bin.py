"""The built-in bin() method returns the binary version of a specified integer. The result will
always start with '0b'"""

x = bin(24)
y = bin(256)
print(x)  # This will print the binary version of 24
print(y)  # This will print the binary version of 256

z = int(x, 2)  # This is how we can reverse binary operation. 2 specifies the base
print(z)  # This will print 24 as integer
