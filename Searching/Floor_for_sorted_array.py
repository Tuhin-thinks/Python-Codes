"""Given a sorted array arr[] of size N without duplicates, and given a value x. Find the floor of x in given array. Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the array and element whose floor is to be searched. Last line of input contains array elements.

Output:
Output the index of floor of x if exists, else print -1 (0 based Indexing).

User Task:
The task is to complete the function findFloor() which finds the floor of x.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ arr[i] ≤ 1018
0 ≤ X ≤ arr[n-1]

Example:
Input:
3
7 0
1 2 8 10 11 12 19
7 5
1 2 8 10 11 12 19
7 10
1 2 8 10 11 12 19

Output:
-1
1
3

Explanation:
Testcase 1: No element less than 0 is found. So output is "-1".
Testcase 2: Number less than 5 is 2, whose index is 1(0-based indexing).
Testcase 3: Number less than or equal to 10 is 10 and its index is 3."""


# Complete this function
def findFloor(A, N, X):
    # Your code here
    if min(A) < X:
        if X in A:
            return A.index(X)
        else:
            count = 0
            prev = A[0]
            for i in A[1:]:

                count += 1
                if i < X:
                    prev = count
                else:
                    return prev

            return prev
    elif min(A) == X:
        return A.index(X)
    else:
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():
    T = int(input())
    while T > 0:
        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]

        A = [int(x) for x in input().strip().split()]

        print(findFloor(A, N, X))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends