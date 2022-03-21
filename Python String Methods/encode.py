"""The encode() method encodes the string, using the specified encoding. If no encoding is specified
UTF-8 will be used. The syntax is string.encode(encoding=encoding, errors=errors)."""

our_text = "My name is Ståle."  # This is our text with some extra character
encoded_text = our_text.encode()  #This will encode the text with UTF-8
print(encoded_text)  # This will print out the encoded text
