#! /bin/usr/env python
import sys
import os

if len(sys.argv) > 1:
    time = "+" + sys.argv[1]
else:
    time = "now"

def sleep(when):
    os.system("sudo shutdown -s " + when)

sleep(time)
