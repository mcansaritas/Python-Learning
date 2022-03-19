"""The built-in eval() method evaluates the specified expression, if the expression is a Legal
Python statement, it will be executed. The syntax is eval(expression, globals, locals). Expression
is a string that will be evaluated as Python code. Globals and locals are optional."""

x = 'print("Mertcan")'
eval(x)

# It evaluates the code that we write and understand it is executable. Then executes it