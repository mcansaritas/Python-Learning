"""The built-in locals() method return the local symbol table as a dictionary. A symbol table
contains necessary information about the current program. The syntax is locals()."""

x = locals()
print(x)  # It prints out the locals in our code
print(x["__file__"])  # It prints out the file

