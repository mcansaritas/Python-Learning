"""The built-in compile() method returns the specified source as a code object, ready to be
executed. The syntax is compile(source, filename, mode, flag, dont_inherit, optimize). Source
is required, and it is the source to be compiled. Filename is required, it specifies the name of
the file that the source comes from. Mode is required, legal values are eval, exec, and single.
Flag is optional and shows how to compile, don't inherit is optional and shows how to compile
the source, and optimize is optional defines the optimization level of compiler."""

x = compile('print("Mertcan")\nprint(50)', 'test', 'exec')
exec(x)