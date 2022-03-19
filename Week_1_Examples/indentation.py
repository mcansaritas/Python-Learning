"""Here we are going to test how indentation works. We have a variable named "my_var" and our
line of code is testing if our variable if it is equal to 2 or bigger"""

my_variable_list =[2, 3, 4]

for x in my_variable_list:
    if x == 3:
        print("My variable is {} and it is equal to 3".format(x))
    elif x > 3:
        print("My variable is {} and it is bigger than 3".format(x))
    else:
        print("My variable is {} and it is smaller than 3".format(x))

"""For understanding purposes we created a for loop. We are going to check every element in 
the list one by one and print its status when we compare it with 3."""