"""There is "if" statement. If indentation is used, then it mean we are in the condition with 
line of the code. If it is not indented, then we are out of condition. We can also use "else"
and "elif" statement if required."""

if True:
    print("This is our first line of code with 'if' statement")
    print("If statement woks if 'if' statement is true.")

print("-"*30)

if not False:
    print("If statement is 'not False' so it means True")
    print('That is why print statements are written')

my_variable = 10

if my_variable > 10:
    print("My integer is {} and it is bigger than 10".format(my_variable))
elif my_variable < 10:
    print("My integer is {} and it is smaller than 10".format(my_variable))
else :
    print("My integer is {} and it is equal to 10".format(my_variable))
