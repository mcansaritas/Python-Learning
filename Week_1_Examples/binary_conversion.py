"""There is a possibility that we need to convert a decimal into binary. We can use bin method
for that. Below we can see an example. After conversion we can revert it to decimal as well."""

decimal = 255
binary = bin(decimal)
print(binary)
convertion_decimal = int(binary, 2)
print(convertion_decimal)