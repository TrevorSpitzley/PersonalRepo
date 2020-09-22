#! /bin/usr/env python
import sys

if len(sys.argv) > 1:
    param = sys.argv[1]
else: 
    param = "reversal"


def rev(string):
    word = ""
    for char in string:
        word = char + word
    return word

print(rev(param))
