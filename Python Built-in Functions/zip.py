"""The zip() function returns a zip object, which is an iterator of tuples where the first
item in each passed iterator is paired together, and then the second item in each passed
iterator are paired together etc.If the passed iterators have different lengths, the iterator
with the least items decides the length of the new iterator. The syntax is zip(iterator1,
 iterator2, iterator3 ...)."""

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(tuple(x))

print("-"*30)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(tuple(x))

# If one tuple contains more items, these items are ignored
