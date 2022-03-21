# The copy() method returns a copy of the list. The syntax is list.copy().

fruits = ['apple', 'banana', 'cherry', 'orange']  # This is our first list
new_list = fruits.copy()  # This is a copied new list
print(fruits)  # Print the old list
print(new_list)  # Print the new list

print('-'*30)

new_list.append('cucumber')  # This will append to new list
print(fruits)

print(new_list) # Print the new list after append() method
print(id(new_list))  # Print the new list's memory id
print(id(fruits))  #Print the old list's memory id

# We can see that our copied new list and old list is not the same.
