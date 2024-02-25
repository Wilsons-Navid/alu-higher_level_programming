#!/usr/bin/python3
def uniq_add(my_list=[]):
    answer = 0
    for x in set(my_list):
        answer += x
    return (answer)
