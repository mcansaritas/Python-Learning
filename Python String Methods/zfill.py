"""The zfill() method adds zeros at the beginning of the string, until it reaches the specified
length. If the value of the len parameter is less than the length of the string, no filling is
done. The syntax is string.zfill(len)."""

our_text = "50"  # This is our text
zero_filled = our_text.zfill(10)  # This will fill the string with zeros until it's 10 character long
print(zero_filled)  # This fill print out the filled text

print('-'*30)

a = "hello"  # This is our text
b = "welcome to the jungle"  # This is our text
c = "10.000"  # This is our text

print(a.zfill(10))  # This will print out the filled text
print(b.zfill(10))  # This will not print out the filled text, because of length issues
print(c.zfill(10))  # This will print out the filled text
