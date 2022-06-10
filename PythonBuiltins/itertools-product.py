"""
Problem solved: https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
"""
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

AxB = product(*[a, b])
print(*list(AxB))