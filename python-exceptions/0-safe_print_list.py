#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if count >= x:
                break
            print(element)
            count += 1
    except TypeError:
        print("Error: my_list must be iterable.")
    return count
