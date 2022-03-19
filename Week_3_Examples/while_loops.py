"""We are going to learn about 'while' loops. The while loops will work as long as the statement
is True. When the code block is done, it will go to the top and check the expression again. It
will work until the while statement is not True"""

my_counter = 1

while my_counter < 5:  # It will start working beucase counter is smaller than 5
    print("My counter will increment and stop at 4 and counter is {}".format(my_counter))
    my_counter += 1  # This will increment every time we return to the loop
