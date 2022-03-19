"""The built-in slice() method returns a slice object. A slice object is used to specify how to
slice a sequence. You can specify where to start the slicing, and where to end. You can also
specify the step, which allows you e.g. slice only every other item. The syntax is
slice(start, end, step). Start is optional and it is integer number specifying at which position
to start the slicing (default is 0). End is an integer number specifying at which position to end
the slicing. Step is optional and it is an integer number specifying the step of slicing, default
value is 1."""

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)  # We are saying that stop slicing after 2 slices
print(a[x])  # This will print out the result

print("-"*30)

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)  # We are saying that start from position 3, and slice to position 5
print(a[x])  # This will print out the result

print("-"*30)

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)  # We are saying that return us every 3 item in the tuple
print(a[x])  # This will print out the result
