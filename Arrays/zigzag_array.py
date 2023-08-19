# Problem: convert array into zig-zag fashion
# https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion1638/1

class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):

        flag = False
        i = 0
        while i < n - 1:
            if not flag and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            elif flag and arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

            flag = not flag
            i = i + 1


# {
# Driver Code Starts
# Initial Template for Python 3

import sys


def isZigzag(arr, n):
    f = 1

    for i in range(1, n):
        if f:
            if arr[i - 1] > arr[i]:
                return 0
        else:
            if arr[i - 1] < arr[i]:
                return 0
        f = f ^ 1

    return 1


t = int(input())
while t:
    n = int(input())
    arr = [int(x) for x in input().split()]
    ob = Solution()
    ob.zigZag(arr, n)
    check = isZigzag(arr, n)

    if check:
        print("1")
    else:
        print("0")

    t -= 1

sys.exit(0)
