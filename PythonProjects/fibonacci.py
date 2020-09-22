#! /bin/usr/env python
import sys

if len(sys.argv > 1):
    number = int(sys.argv[1])
else:
    number = 10

def fib(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


for x in range(1, number + 1):
    print(str(fib(x)) + ", ", end="")

