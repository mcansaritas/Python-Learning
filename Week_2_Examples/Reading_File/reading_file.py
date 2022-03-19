"""Python has an ability to read and write files. When we print the open function for the
file we can see its reference."""

first_reading = open(r"C:\Users\saritas\Python Projects\Kirk Byers Network Automation\Week_2_Examples\Reading_File\read.txt", "r")
output = first_reading.read()
print(output)  # It shows the output in the file
print(first_reading)  # It shows the reference of this reading process.

print("-"*30)

second_reading = open(r"C:\Users\saritas\Python Projects\Kirk Byers Network Automation\Week_2_Examples\Reading_File\read.txt", "r")
each_line = second_reading.readline()
print(each_line)  # This reads the string line by line including \n.
each_line = second_reading.readline()
print(each_line)
each_line = second_reading.readline()
print(each_line)

"""Readline can be used to read the string line by line not at once."""

print("-"*30)

third_reading = open(r"read.txt", "r")
all_lines = third_reading.readlines()
print(all_lines)  # This returns us with a list and we can see all lines.

print("-"*30)

last_reading = open(r"read.txt", "r")
lines = last_reading.read()
split_lines = lines.splitlines()
print(split_lines)
