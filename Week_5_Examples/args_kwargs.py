"""Let's assume that we have a list and this list consists of 3 elements. And we need 3 variable
in our function as well. It would be nice that we would pass in the list to our function.
With *args we can send the list or tuple into the function."""

my_list = ["1.1.1.1", "admin", "password"]
my_tuple = ("2.2.2.2", "cisco", "nokia")

def ip_username_password(ip_address, username, password):
    print("My IP address is %s, and you can see username password below." % ip_address)
    print(username)
    print(password)

ip_username_password(*my_list)
ip_username_password(*my_tuple)

"""The same thing is valid for dictionaries. Keep in mind that the key name must be the same
with arguments in function. It is called **kwags. It will mean that conver this to the key
value pairs. Don't treat as a single element."""

my_dictinoary = {"ip_address": "3.3.3.3", "username": "Python", "password": "Dictionary"}
ip_username_password(**my_dictinoary)

"""We need to careful about passing mutable into a function. When you pass in a mutable
like a list, it is very easy to modify the thing that you passed in. We can test it."""

def list_append(list):
    print(list)
    list.append(123)

my_list = ["whatever"]
list_append(my_list)

print(my_list)

"""We can use the same variable inside and outside the function. They are totally different
from each other. Variable in the function is only used in function. If Python can't find the
variable in the function, it will look for global variables."""

ip_address2 = "192.168.1.1"

def ip_print(ip_address, username = "admin", password = "Cisco123"):
    print(f"My first IP address is {ip_address}")
    print(f"My second IP address is {ip_address2}")
    print(username)
    print(password)

ip_print("4.4.4.4")