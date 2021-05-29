"""
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.

Input:
The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and second line will be the elements of the array.

Output:
For each test case the output will be the majority element of the array. Output "-1" if no majority element is there in the array.

User Task:
The task is to complete the function findMajority() which finds the majority element in the array. If no majority exists, return -1.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T<= 100
1 <= N <= 107
0 <= Ai <= 106

Example:
Input:
2
5
3 1 3 3 2
3
1 2 3

Output:
3
-1

Explanation:
Testcase 1: Since, 3 is present more than N/2 times, so it is the majority element.
Testcase 2: Since, each element in {1,2,3} appears only once so there is no majority element.
"""


# Complete this function
def majorityElement(A, N):
    # Your code here
    weight_dict = {}
    for elem in A:
        if elem not in weight_dict.keys():
            weight_dict[elem] = 1
        else:
            weight_dict[elem] += 1

    for item, weight in weight_dict.items():
        if weight > int(N / 2):
            return item
    return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while T > 0:
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(majorityElement(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends