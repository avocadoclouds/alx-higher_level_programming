#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxx = max(a_dictionary)
    return maxx