"""The built-in sorted() method returns a sorted list of the specified iterable object. You can
specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted
numerically. The syntax is sorted(iterable, key=key, reverse=reverse)."""

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)  # This sorts out the elements in the tuple
print(x)  # This prints out the sorted tuple

print("-"*30)

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)  # This reverse sorts out the elements in the tuple
print(x)  # This prints out the reverse sorted tuple
