#! /bin/usr/env python
import sys

if len(sys.argv) > 1:
    number = int(sys.argv[1])
else:
    number = 10

def fact(num):
    if num >= 0:
        if num == 0:
            return 1
        else:
            return num * fact(num - 1)
    else:
        return 0


for x in range(1, number + 1):
    print(str(x) + "! equals " + str(fact(x)))
