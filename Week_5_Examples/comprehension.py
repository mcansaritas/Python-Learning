"""There is a concept named comprehension. With comprehension we can change a list to
another list. Let's look into an example"""

list = [1, 2, 3, 4, 5, 6, 7]
list2 = [x**2 for x in list]
print(list2)
list3 = [x**3 for x in list]
print(list3)