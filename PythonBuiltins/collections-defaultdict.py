"""
Problem solved: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
"""

from collections import defaultdict

n, m = map(int, input().split())
group_a_dict = defaultdict(list)
for index in range(n):
    group_a_dict[input()].append(index + 1)

d = defaultdict(list)

for _ in range(m):
    print(*group_a_dict[input()] or [-1])