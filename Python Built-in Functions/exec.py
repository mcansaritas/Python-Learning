"""The built-in exec() method executes the specified Python code. It accepts large blocks of code
code, unlike eval() method which only accepts a single expression. The syntax is exec(object,
globals, locals)."""

x = 'name = "John"\nprint(name)'
exec(x)

# It executes the line of code we write