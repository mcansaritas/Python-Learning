def smallest_element(x):
    list_length = len(x)
    if list_length == 0:
        return "There is no element in the list"
    elif list_length == 1 :
        return x[0]
    else :
        my_smallest = x[0]
        for i in range(list_length) :
            if x[i] <= my_smallest :
                my_smallest = x[i]
    return my_smallest