"""The built-in next() method returns the next item in an iterator. You can add a return value,
to return if the iterable has reach to its end. The syntax is next(iterable, default)."""

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)  # It prints out apple
x = next(mylist)
print(x)  # It prints our banana
x = next(mylist)
print(x)  # It prints our cherry

print("-"*30)

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)  # It prints out apple
x = next(mylist, "orange")
print(x)  # It prints out banana
x = next(mylist, "orange")
print(x)  # It prints out cherry
x = next(mylist, "orange")
print(x)  # Since it is end of the list, it prints our orange
