#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print("Number of argument(s):", num_arguments)

    if num_arguments == 0:
        print(".", end="\n\n")
    else:
        print("Arguments:")
        for i, arg in enumerate(arguments, 1):
            print("{}: {}".format(i, arg))

        print()
