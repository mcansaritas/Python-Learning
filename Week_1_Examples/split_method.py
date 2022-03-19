"""There is a split function in Python and we can split string based on our desire. By default
it split using whitespace. Let's try it and what is the output."""

ip_address = "192.168.1.2"
split_ip_address =  ip_address.split(".")  # This is going to split using "."
print(split_ip_address)  # This returns to us a list.

print("-"*30)

sentence = "This is a sentence."
split_sentence = sentence.split()
print(split_sentence)

print("-"*30)

paragraph = """Hi,
my
name
is
Mertcan"""

split_paragraph = paragraph.split("\n")
print(split_paragraph)

print("-"*30)

paragraph_split = paragraph.splitlines()
print(paragraph_split)

print("-"*30)

print(id(split_paragraph))
print(id(paragraph_split))
print(split_paragraph is paragraph_split)

"""We can see that IP address is split using "." and our sentence is split based on whitespace
There is a way to make it together again. It is done with join method."""

paragraph_split

join_sentence = " ".join(split_sentence)
join_ip_address = ".".join(split_ip_address)
join_paragraph = "\n".join(split_paragraph)
print(join_sentence)
print(join_ip_address)
print(join_paragraph)


