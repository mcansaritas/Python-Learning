"""There are some special characters which mean something different for Python. As an example
we can say that \t is tab and \n is enter. Let's create a variable and enter a Windows path."""

my_path = "C:\Windows\newdirectory\test"  # There are special characters that we talked about.
print(my_path)
my_path1 = r"C:\Windows\newdir\test" # Raw input block special characters, and behaved normal
print(my_path1)

"""We can see that without raw string, there is enter and tab in the output. But when we write
raw string with "r" we can see that they are not included in the output."""