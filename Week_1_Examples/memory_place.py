"""We can see where our variables are stored. It is related about the type of data is mutable
or unmutable. Lists and dictionaries are mutable and other data types are not mutable. Let's 
test them and see what is the output."""

variable1 = "String"
variable2 = variable1
variable2 = variable2+"is changed"  # We are changing the string here.

print(id(variable1))
print(id(variable2))
print(variable1 is variable2)  # This is testing if they are in the same memory space.

my_list = [1, 2, 3]
my_list_2 = my_list
print(id(my_list))
print(id(my_list_2))
print(my_list is my_list_2)  # This is testing if they are in the same memory space.

"""We can see that the variable is changed so the memory that is located."""