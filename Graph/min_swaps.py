"""
Given an array of integers. Find the minimum number of swaps required to sort the array in non-decreasing order.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the no of element of the array A[ ]. In the next line are N space separated values of the array A[ ] .

Output:
For each test case in a new line output will be an integer denoting  minimum umber of swaps that are  required to sort the array.

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[] <= 106

User Task:
You don't need to read input or print anything. Your task is to complete the function minSwaps() which takes the array arr[] and its size N as inputs and returns an integer denoting the minimum number of swaps required to sort the array. If the array is already sorted, return 0. 

Expected Time Complexity: O(NlogN).
Expected Auxiliary Space: O(N).

Example(To be used only for expected output):
Input:
2
5
1 5 4 3 2
4
8 9 16 15

Output:
2
1

Explanation:
Test Case 1: We need two swaps, swap 2 with 5 and 3 with 4 to make it sorted. 
"""


# return the minimum number of swaps required to sort the arra
def minSwaps(arr, N):
    # Code here
    value_to_pos = dict()
    #pos_to_value = dict()

    for pos, val in enumerate(sorted(arr)): #O(n log n)
        value_to_pos[val] = pos
        #pos_to_value[pos] = val
    #print(value_to_pos)
    #print(pos_to_value)

    visited = [False for _ in range(len(arr))]
    counts = 0
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True

            if arr[i] == value_to_pos.get(arr[i]):
                continue
            else:
                tmp = value_to_pos.get(arr[i])
                while not visited[tmp]:
                    visited[tmp] = True
                    tmp = value_to_pos.get(arr[tmp])
                    counts += 1

    return counts

# solution contributed by: Sebastian Widmann

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(minSwaps(arr, n))

# } Driver Code Ends