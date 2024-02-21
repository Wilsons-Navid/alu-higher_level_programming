#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord('a') <= ord(i) <= ord('z')+ 1):
            i = chr(ord(i)-32)
    print("{}".format(i), end="")
