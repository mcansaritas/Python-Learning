"""We saw that we can read text files. Also, we can  write into using Python. Let's do some
examples about this and learn how we can do that. the output is showing is how many characters
are sent to the file."""

write_file = open(r"output.txt", "w")
print(write_file.write("We are going to write a file from Python."))
write_file.flush()

"""When we check the file we can see that our line is written by Python. If we write another
thing to the file, it will override the first one. Let's try this."""

write_file = open(r"output.txt", "w")
print(write_file.write("We are testing if second write overrides the first one."))
write_file.flush()