"""When there is a error or problem in our line of code, the run is stoppedi and an error
is written to the terminal. In order to override this behavior we can use try and except
structure. Let's write some code and see how does it work."""

# Let's try get an key from an empty dictionary.

my_dictionary = {}
#print(my_dictionary["Key"])  # We will try to get key named 'key', but our dictionary is empty.

# We can see that we get an KeyError.

try:
    print(my_dictionary["key"])
except KeyError:
    print("I am not able to find the key in our dictionary")

print("-"*30)

try:
    print(my_dictionary["key"])
except KeyError:
    print("I am not able to find the key in our dictionary")
#    raise 

# When raise statement is specified, our line of code is stopped and exception is written.

print("-"*30)

try:
    print(my_dictionary["search"])
except KeyError as hata:
    print(hata.__class__)  # It prints out the class of our exception
    print(hata)  # It prints out the name of the key we search
    print("We saw an exception and print the information")  # It prints this statement

print("-"*30)

try:
    print(my_dictionary["chassis"])
except KeyError:
    print("I am not able to find the key in our dictionary")
finally:
    print("This statement will be printed every time")
