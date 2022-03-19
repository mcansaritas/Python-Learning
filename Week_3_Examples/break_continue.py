"""There are some operations that can change how the loops are working. They are break, continue
and pass. Break statement breaks the loop and quits the for statement, continue jumps to the
loop, and pass it makes our code do nothing."""

loop_list = [1, 2, 3]  # We have a list here with 3 elements in it

for element in loop_list:  # The for loop with loop_list start working
    print(element)  # It will print the first element in the list
    break  # It will break the for loop after first element

# We can see that only the first element is printed. The others are not printed.

print("-"*30)

for element in loop_list:   # The for loop with loop_list start working
    print(element) # It will print the every element in the list
    continue  # This statement will make it to return for loop
    print("We are checking how continue is working")  # This statement won't be printed

for element in loop_list:   # The for loop with loop_list start working
    pass  # This will make our code do nothing without any Error
