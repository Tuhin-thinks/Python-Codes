"""
problem link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
"""n3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_a = abs(z-x)
    cat_b = abs(y-z)
    if cat_a > cat_b:
        return "Cat B"
    elif cat_b > cat_a:
        return "Cat A"
    else:
        return "Mouse C"
    

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)
