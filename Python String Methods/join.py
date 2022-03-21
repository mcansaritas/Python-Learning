"""The join() method takes all items in an iterable and joins them into one string. A string
must be specified as a separator. The syntax is string.join(iterable)."""

my_tuple = ('John', 'Peter', 'Vicky')  # This is a tuple for join method
join_them = ', '.join(my_tuple)  # This is joining them with with ', '
print(join_them)  # This will print out the joined string

my_dictionary = {"name": "John", "country": "Norway"}  # This is our dictionary
separator = "Mertcan"  # This is our separator to join the dictionary

joined_dictionary = separator.join(my_dictionary)  # This will join the dictionary with separator
print(joined_dictionary)  # This will print out joined dictionary. The keys are joined not values
