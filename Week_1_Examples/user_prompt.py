"""We are going to learn how we can gather user input with PythonWe need to use input method
 for this. Let's write some example for this and see how does it work."""

my_variable1 = input("Please write your first integer to sum: ")
my_variable2 = input("Please write your second integer to sum: ")

sum = my_variable1 + my_variable2  # It sums as a string.
print(sum)
sum = int(my_variable1) + int(my_variable2)  # It sums as a integer.
print(sum)

"""As you can see from above output. It didnt do the sum that we want. It understand the input
as string and it added to each other as a string."""

ip_address = input("Please enter an IP address: ")
print("Your IP address that you enter is {}".format(ip_address))