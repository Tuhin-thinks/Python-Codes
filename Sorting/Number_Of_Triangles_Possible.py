"""
Problem Statement:
Given an unsorted array arr[] of positive integers. Find the number of triangles that can be formed with three different array elements as lengths of three sides of triangles.

Example 1:

Input: N = 3, arr[] = {3, 5, 4}
Output: 1
Explanation: A triangle is possible
with all the elements 5, 3 and 4.

Example 2:

Input: N = 5, arr[] = {6, 4, 9, 7, 8}
Output: 10
Explanation: There are 10 triangles possible
with the given elements like (6,4,9), (6,7,8),...

Your Task: This is a function problem. You only need to complete the function findNumberOfTriangles() that takes arr[] and N as input parameters and returns the count of total possible triangles.

Expected Time Complexity: O(N2).
Expected Space Complexity: O(1).

Constraints:
3 <= N <= 103
1 <= arr[i] <= 103
"""

''' Your task is to return the total no of triangles possible.'''


def findNumberOfTriangles(arr, n):
    # code here
    arr.sort()
    count = 0
    for i in range(n - 2):
        c = i + 1
        for j in range(i + 1, n):
            while (c < n and arr[i] + arr[j] > arr[c]):
                if c > j:
                    count += c - j
                c += 1
    return count


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = list(map(int, input().strip().split()))
        print(findNumberOfTriangles(arr, size))

# } Driver Code Ends