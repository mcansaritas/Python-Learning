"""The built-in globals() method returns the global symbol table as a dictionary. A symbol table
contains necessary information about the current program. The syntax is globals()."""

x = globals()
print(x)
print(x["__file__"])

"""Symbol table is a data structure which contains all necessary information about the program.
These includes variable names, methods, classes, etc. Global symbol table stores all information
related to the global scope of the program, and is accessed in Python using globals() method."""

"""We can also change the value of global variables by using globals() function. the changed
value also updated in the symbol table."""