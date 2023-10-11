#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_ = float("-inf")
    best_k = None
    for k, v in a_dictionary.items():
        if v > max_:
            max_ = v
            best_k = k
    return best_k
