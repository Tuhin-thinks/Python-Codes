"""
Problem solved: https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
"""
# !/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    d = defaultdict(int)
    for i in arr:
        if i > 0:
            d['pos'] += 1
        elif i < 0:
            d['neg'] += 1
        else:
            d['zero'] += 1

    # find ratios of positive, negative and zero
    pos_ratio = d['pos'] / len(arr)
    neg_ratio = d['neg'] / len(arr)
    zero_ratio = d['zero'] / len(arr)

    # print the ratios
    print(f"{pos_ratio:.06f}")
    print(f"{neg_ratio:.06f}")
    print(f"{zero_ratio:.06f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
