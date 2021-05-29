"""
problem statement can be found here:
https://www.hackerrank.com/challenges/maximum-subarray-sum/problem?
"""
import math
import os
import random
import re
import sys
import bisect


# Complete the maximumSum function below.
def maximumSum(a, m):
    mm, pr = 0, 0
    a1 = []
    for i in a:
        pr = (pr + i) % m
        mm = max(mm, pr)
        ind = bisect.bisect_left(a1, pr + 1)
        if ind < len(a1):
            mm = max(mm, pr - a1[ind] + m)
        bisect.insort(a1, pr)
    return mm


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
