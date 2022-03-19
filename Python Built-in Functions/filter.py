"""The built-in filter() method returns an iterator where the items are filtered through a function
to test if the item is acceptable or not. The syntax is filter(function, iterable)."""

ages = [5, 12, 17, 18, 24, 32]

def myfunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myfunc, ages)
for elements in adults:
    print(elements)

# It is going to test the values inside the list named ages, and filter which values are accepted
