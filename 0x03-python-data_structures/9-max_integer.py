#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maxx = 0
        for i in my_list:
            if i > maxx:
                maxx = i
        return maxx
