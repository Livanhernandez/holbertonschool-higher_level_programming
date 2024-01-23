#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse = reversed(my_list)
    for i in reverse:
        print("{:d}".format(i))
