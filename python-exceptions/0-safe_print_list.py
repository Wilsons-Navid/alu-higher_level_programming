#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            print(element, end=' ')
            count += 1
            if count == x:
                break
        else:
            print()  # Print a new line if the loop completes without breaking
    except TypeError:
        print("Error: my_list must be iterable.")
    return count
