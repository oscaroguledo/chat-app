#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    mod = 24
    if "PM" in s or "pm" in s:
        num = int(s[0:2])
        if num==12:
            num= mod-num
        else:
            num =mod-(12-num)
        ns = f"{abs(num)}"+s[2:-2]
        print(ns)
        return ns
    if "AM" in s or "am" in s:
        num = int(s[0:2])
        if num == 12:
            num = 12-num
        ns = f"0{num}"+s[2:-2]
        print(ns)
        return ns 
    

if __name__ == '__main__':

    #s = input()

    result = timeConversion("12:45:54PM")
"""
    fptr.write(result + '\n')

    fptr.close()"""
