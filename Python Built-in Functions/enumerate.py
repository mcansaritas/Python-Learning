"""The built-in enumerate() method takes a collection and returns it as an enumerate object.
The enumerate() method adds a counter as the key of the enumerated object. The syntax is
enumerate(iterable, start). The iterable is an object that we can iterate, and start is a number
defining the start number of the enumerate object and default is 0."""

x = ("apple", "orange", "banana", "cherry")
y = enumerate(x)

for element in y:
    print(element)

# We can see that it prints index and index's value from our tuple