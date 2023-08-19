# Problem source: https://practice.geeksforgeeks.org/problems/sorted-subsequence-of-size-3/1
# Sorted subsequence of size 3

from collections import defaultdict


class Solution:
    def find3number(self, A, n):

        max_a = defaultdict(lambda: -1)
        min_a = defaultdict(lambda: -1)
        max_e = n - 1
        min_e = 0

        # for min
        for i in range(n):
            e = A[i]
            if e <= A[min_e]:
                min_e = i
                min_a[i] = -1
            else:
                min_a[i] = min_e

        for j in range(n - 1, -1, -1):
            e = A[j]
            if e >= A[max_e]:
                max_e = j
                max_a[j] = -1
            else:
                max_a[j] = max_e

        for i in range(n):
            if min_a[i] != -1 and max_a[i] != -1:
                seq = (A[min_a[i]], A[i], A[max_a[i]])
                return seq

        return []


# {
# Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(100000)


def isSubSeq(arr, lis, n, m):
    if m == 0:
        return True
    if n == 0:
        return False
    if arr[n - 1] == lis[m - 1]:
        return isSubSeq(arr, lis, n - 1, m - 1)
    return isSubSeq(arr, lis, n - 1, m)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = Solution().find3number(arr, n)
    # print(lis)
    # print(isSubSeq(arr, lis, n, len(lis)))
    if len(lis) != 0 and len(lis) != 3:
        print(-1)
        continue
    if len(lis) == 0:
        print(0)
    elif lis[0] < lis[1] and lis[1] < lis[2] and isSubSeq(arr, lis, n, len(lis)):
        print(1)
    else:
        print(-1)
