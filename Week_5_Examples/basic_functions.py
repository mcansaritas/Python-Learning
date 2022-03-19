"""We are going to exercise how we can write correct functions. In order to write a function
we need to define them with def statement. The line of code is processed from up to bottom. 
They need to return  to a value every time."""

def ip(ip_address):
    print("My IP address is {}".format(ip_address))

ip("10.10.10.1")  # This will call the function for 10.10.10.1
ip("10.10.10.2")  # This will call the function for 10.10.10.2

# Here there is no return value needed. Because we not expecting to return to a value.

print("-"*30)

"""There is a possibility that we can add more arguments to the functions. We must specify
them when we call the function. They are assigned based on their position. So, we need to know
function's variable sequence."""

def ip_username_password(ip_address, username, password):
    print("My IP address is {}, and you can see username password below.".format(ip_address))
    print(username)
    print(password)

ip_username_password("1.1.1.1", "admin", "gnegpec")
ip_username_password("1.1.1.2", "admin", "admin")

"""We can call the functions using named arguments. Then the sequence is not important.
Because we name it inline with function variables."""

ip_username_password(ip_address = "10.10.10.1", username = "admin", password = "cisco")

