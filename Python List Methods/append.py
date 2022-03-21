"""The append() method appends an element to the end of the list. The syntax is list.append(
element)."""

fruits = ['apple', 'banana', 'cherry']
print(fruits)  # This is going to print our initial list

print("-"*30)

fruits.append('orange')  # This is going to append a new element to the end of the list
print(fruits)

# At the same time we can add a list to the end of the list

list1 = ['apple', 'banana', 'cherry']  # This is our first list
list2 = ["Ford", "BMW", "Mercedes"]  # This is our second list
list1.append(list2)  # We are going to add list2 to the end of list1
print(list1)  # This will print out the final list1 with updated with the list2
