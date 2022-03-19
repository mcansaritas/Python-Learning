"""There is a chance that we can format string in Python. We can do it using "format" method.
Let's write some examples and see what is the output."""

ip_address_1 = "1.1.1.1"
ip_address_2 = "2.2.2.2"
ip_address_3 = "3.3.3.3"

print("{}{}{}".format(ip_address_1, ip_address_2, ip_address_3))
print("{} {} {}".format(ip_address_1, ip_address_2, ip_address_3))
print("{:>20} {:>20} {:>20}".format(ip_address_1, ip_address_2, ip_address_3))
print("{my_ip1:^20} {my_ip2:^20} {my_ip3:^20}".format(my_ip1=ip_address_1, my_ip3=ip_address_2, my_ip2=ip_address_3))
print(f"{ip_address_1}{ip_address_2}{ip_address_3}")
print("These are my IP address %s, %s, and %s" %(ip_address_1, ip_address_2, ip_address_3))

"""In Python there is a method called *args. We can do it with lists.
Let's try it with a line of code."""

ip_address = "192.168.1.2"
octets = ip_address.split(".")
print(octets)
print("My first octet is {}, second octet is {}, third octet is {} and last octet is {}.".format(*octets))
