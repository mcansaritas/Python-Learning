"""There are some operations that we can do with lists. List is a sequencial data. It is using
indexing. Lists are written with square brackets []. We are going to set operations like pop,
append and extend."""

from pyparsing import match_only_at_col


my_list = []  # We have created an empty list.
print(type(my_list))  # It is going to write as class list.

print("-"*30)

my_list.append("There")
print(my_list)  # It will print a list with one element.
print(len(my_list))  # It will print the length of the list which is 1.
print(my_list[0])  # It will print the first element in the list.
print(my_list.index("There"))  # We can search for the index of a specific element.

print("-"*30)

print(my_list + [1, 2, 3])  # It is concatenation, but it does not change the original list.
my_list.extend([1, 2, 3, 4, 5])  # It is used to add multiple elements at a time.
print(my_list)

print("-"*30)

print(my_list.pop(0))  # This removes the first element in the list.
print(my_list)
print(my_list.pop())  # This removes the last element in the list.
print(my_list)
del my_list [0]  # This will delete the first element in the list.
print(my_list)

print("-"*30)

my_list.remove(3)  # This will be used to remove a specific element in the list.
print(my_list)

# As we talked before lists are mutables. Let's go and test this one.

new_list = my_list  # We are going to assign a new list to already existing one.
print(new_list is my_list)  # This is going to check if they are same im memory.
new_list.append("new list and first one the same")  # This line will be added to both of them.
print(new_list)
print(my_list)


