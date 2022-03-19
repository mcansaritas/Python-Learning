"""Right now we are going to import a function outside of our code. Also we are going
to import a file like a package. Let's write our code."""

import smallest_number_in_list  # We are importing our Python code from outside.
from IPChecker import ip_checker

check_1 = smallest_number_in_list.smallest_element([3, 2, 1])
check_2 = smallest_number_in_list.smallest_element([-1, -2, -3])

print(check_1)
print(check_2)

print("-"*30)

ip_checker.ipchecker ("1.1.1.1")

print("-"*30)

ip_checker.ipchecker ("255.255.255.256")

print("-"*30)

ip_checker.ipchecker ("1.1.1.a")

print("-"*30)

ip_checker.ipchecker ("1...")