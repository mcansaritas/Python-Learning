""" We don't have to convert a list into sets. We can create a set with { } and it is
similar to dictionaries. We can do some operations like intersection, union, and
symmetric differences. Let's write some code for practicising."""

first_set = {1, 2, 3, 4}
second_set = {3, 4, 5, 6}

print(first_set | second_set)  # This is set union. It will show us with all unique values
print(first_set & second_set)  # Thi is set intersection. It will shows us with intesection
union_set = first_set.union(second_set)  # This is how we can do without special character
print(union_set)
intersect_set = first_set.intersection(second_set)  # This is how we can do without special character
print(intersect_set)

print("-"*30)

print(first_set - second_set)  # This returns the difference of first_set and second_set
print(second_set - first_set)  # This returns the difference of second_set and first_set
print(first_set ^ second_set)  # This returns the symmetric difference of 2 sets

print("-"*30)

print(first_set.difference(second_set))
print(second_set.difference(first_set))
print(first_set.symmetric_difference(second_set))