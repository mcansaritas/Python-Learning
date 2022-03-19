"""Our first example was with the string in our code. Also, we can use regular expression
reading an external file with Python. Then we can use regex for what we want. Let's run
some code and see how we can use."""

import re

with open(r"regex.txt") as reader:
    output = reader.read()

print(output)
print(re.search(r"^There$", output))  # This couldn't find anything because it understand the text as whole
print(re.search(r"^There", output, flags=re.M))  # This could find with checking all lines and understand the beginning of string

print("-"*30)

with open(r"version.txt") as reader:
    output = reader.read()

print(output)

print("-"*30)

print(re.search(r"TiMOS-C-(.*) cpm.*", output, flags=re.DOTALL).group(1))  # This will search for TiMOS release
print(re.search(r"TiMOS-C-(?P<Release>.*) cpm.*", output, flags=re.DOTALL).groupdict())
release = re.search(r"TiMOS-C-(?P<Release>.*) cpm.*", output, flags=re.DOTALL)
print(release.groupdict())  # This will print out our regular expression and its value

#We can give a name for regular expression and then we can print it as dictionary.

print("-"*30)

print(re.split(r"19.10.R1", output, flags=re.M))  # We can split based on regex findings.
print(re.sub(r"19.10.R1", "Change", output, flags=re.M))  # We can find a matching string and change it with another string