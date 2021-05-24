#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    last_state = path[0]
    count = 0
    u_count = 0
    d_count = 0
    for state in path[1:]:
        if last_state != state:  # state change
            if state == 'D':
                count += 1
                print("state change to D, count increased to ", count)
            last_state = state
    return count
            
            

if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)
