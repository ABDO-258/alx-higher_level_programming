#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        new_dictionary = dict(sorted(a_dictionary.items(),
                                     key=lambda item: item[1],
                                     reverse=True))
        return next(iter(new_dictionary))
