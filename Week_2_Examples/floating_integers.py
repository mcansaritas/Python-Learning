"""We are able to use floating numbers in Python. Let's write some examples and see how does
it work."""

from decimal import Rounded


first_integer = 15
first_float = 2.15
second_float = 3.18
third_float = 2.75343123

minus_operation = second_float - first_float
print(minus_operation)
print(float(first_integer))

"""We can see that the minus operation output is not what we expected. The reason for that
the operation is based on binary. After that it is converted back to decimal. We can round
float numbers."""

print(round(third_float, 2))  # It rounds for 2 digits.
print(round(third_float, 5))  # It rounds for 5 digits.

