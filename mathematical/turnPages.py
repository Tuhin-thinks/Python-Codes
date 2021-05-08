"""
problem link:https://www.hackerrank.com/challenges/drawing-book/problem
"""

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    if p == n or p==n or (n%2 != 0 and p==(n-1)):
        return 0
    else:
        if p <= n/2:
            return p//2
        else:
            return (n//2)-(p//2)
            

if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
