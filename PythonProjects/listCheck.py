#!/usr/bin/env python

# This file is used for comparing two lists.
# If there is an element in the input_list,
# and it is not in the black_list, then it
# will be added to the out_list and printed


def list_check(input_list, black_list):
    out_list = []
    for element in input_list:
        if element not in black_list:
            out_list.append(element)

    return out_list


chars = ['a', 'b', 'c', 'd']
chars2 = ['e', 'f', 'g', 'h']
chars3 = ['a', 'c']
chars4 = ['e', 'h']

ints = [1, 2, 3, 4]
ints2 = [5, 6, 7, 8]
ints3 = [1, 2, 3]
ints4 = [5, 6, 7, 8]

# Should return ['b', 'd']
print(list_check(chars, chars3))
# Should return ['f', 'g']
print(list_check(chars2, chars4))
# Should return [4]
print(list_check(ints, ints3))
# Should return []
print(list_check(ints2, ints4))
# Should return ['e', 'f', 'g', 'h']
print(list_check(chars2, ints))
# Should return [1, 2, 3]
print(list_check(ints3, chars3))
