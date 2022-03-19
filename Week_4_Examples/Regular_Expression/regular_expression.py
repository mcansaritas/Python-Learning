"""We are going learn and test some stuff about regular expression. With regular expression
we are able to find a pattern in texts. It is done with special characters and their meaning
for regular expression. By default regular expression works line by line."""

import re

ip_address = """192.168.1.2
192.168.1.3
""" # This is our IP address and we will work on this one with regex

#print(re.search(r".", ip_address))  # This shows us that there is a match and it is 1
#print(re.search(r".", ip_address).group(0))  # This print out the character that it found which is 1
#
#print("-"*30)
#
#print(re.search(r"..", ip_address))  # This shows us that there is a match and it is 19
#print(re.search(r"..", ip_address).group(0))  # This print out the character that it found which is 19
#
#print("-"*30)
#
#print(re.search(r".*", ip_address))  # This shows us that there is a match it is all string
#print(re.search(r".*", ip_address).group(0))  # It prints out the string that it found which is all string 
#
#print("-"*30)
#
#print(re.search(r"\d+", ip_address))  # This shows us that there is a match and stops at first finding
#print(re.search(r"\d+", ip_address).group(0))  # It prints out the string that it found which is 192
#
#print("-"*30)
#
#print(re.findall(r"\d+", ip_address))  # This shows us that all string that match to regex and it returns a list
#print(re.findall(r"\d+", ip_address)[0])  # This prints out the first element in the list
#
#print("-"*30)
#
#print(re.search(r"[\s\S]+", ip_address))  # This shows that all string is a match
#print(re.search(r"[\s\S]+", ip_address).group(0))  # It prints out the whole string
#
#print("-"*30)

"""Like we said above, regular expression works line by line. It is not operating as multiline.
But we can make it work as multiline. They are called flags and they are M and DOTALL. Let's
test them and see how do they work."""

print(re.search(r"\d+", ip_address, flags=re.M))  # This stops when it finds first matching string
print(re.findall(r"\d+", ip_address, flags=re.M))  # This searches all matching strings

# re.M makes it multiline and findall can find all matching strings

print(re.search(r".+\n", ip_address, flags=re.DOTALL))  # This stops when it founds the first match
print(re.findall(r".+\n", ip_address, flags=re.DOTALL))  # This searchs for all matching strings