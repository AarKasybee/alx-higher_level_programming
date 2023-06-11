#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    m = []
    for i in range(len(my_list)):
        m.append(my_list[idx])
        print("{:d}".format(m[i]))
        idx = idx - 1
