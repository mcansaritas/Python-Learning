"""The built-in reserved() method returns a reversed iterator object."""

alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
    print(x)

# This will reverse the loop and start from d
