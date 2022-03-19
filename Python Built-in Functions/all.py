"""The built-in all() method checks if all items in a list True or not. 
If all of the items are not True, then it will return False. If the iterable object
is empty, the all() function also returns True."""

my_list1 = [True, True, True]  # All items are True
print(all(my_list1))  # It will return True

print("-"*30)

my_list2 = [True, False, True]  # One item is False
print(all(my_list2))  # It will return False, because not all items are True

print("-"*30)

# Iterable objects returns True if empty. They are list, tuple, dictionary.

my_list3 = [1, 2, 3]  # This is a list
print(all(my_list3))  # This will return True because all items are True

print("-"*30)

my_tuple = (0, True, False)  # This is a tuple
print(all(my_tuple))  # This will return False, because not all items are True

print("-"*30)

my_set = {0, 1, 0}  # This is a set
print(all(my_set))  # This will return False, because not all items are True

print("-"*30)

my_dict1 = {1:"Apple", 2:"Orange"}  # This is a dictionary
print(all(my_dict1))  # This will return True, because all items are True

# When used on a dictionary, the all() function checks if all the keys are True, not values.

print("-"*30)

my_dict2 = {}  # This is an empty dictionary
print(all(my_dict2))  # This will return True even if dictionary is empty
