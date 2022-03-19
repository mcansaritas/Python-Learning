"""We are going to learn about Python sets. Sets are not sequenced. Let's write some line of
code and how we can use it. First we need to use list and then convert to sets. Sets can't
have duplicate values."""

from pyparsing import match_only_at_col


my_list = [1, 2, 3, 4, 5, 6, 1, 2, 3]  # This is our list with duplicate values.
print(my_list)  # When we print that we are going to see duplicate values as well.

my_set = set (my_list)  # We are converting our list into a set
print(my_set)  # We are printing it and it removes the duplicate values.
print(type(my_set))  # It will return us class set