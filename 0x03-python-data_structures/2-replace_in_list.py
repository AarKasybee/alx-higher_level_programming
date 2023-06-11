#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    temp_list = my_list
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        temp_list[idx] = element
        return temp_list
