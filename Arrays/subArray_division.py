"""
problem link: https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    ways = 0
    for i in range(len(s)-m+1):
        chocolate_strip = s[i:i+m]
        if sum(chocolate_strip) == d:
            ways += 1
    return ways
            

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
