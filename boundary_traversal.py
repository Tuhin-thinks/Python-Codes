"""
You are given a matrix A of dimensions n1 x m1. The task is to perform boundary traversal on the matrix in clockwise manner.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase two lines of input. The first line contains dimensions of the matrix A, n1 and m1. The second line contains n1*m1 elements separated by spaces.

Output:
For each testcase, in a new line, print the boundary traversal of the matrix A.

Your Task:
This is a function problem. You only need to complete the function boundaryTraversal() that takes n1, m1 and matrix as parameters and prints the boundary traversal. The newline is added automatically by the driver code.

Expected Time Complexity: O(N1 + M1)
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 100
1 <= n1, m1<= 100
0 <= arri <= 1000

Examples:
Input:
4
4 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4
12 11 10 9 8 7 6 5 4 3 2 1
1 4
1 2 3 4
4 1
1 2 3 4
Output:
1 2 3 4 8 12 16 15 14 13 9 5
12 11 10 9 5 1 2 3 4 8
1 2 3 4
1 2 3 4

Explanation:
Testcase1: The matrix is:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
The boundary traversal is 1 2 3 4 8 12 16 15 14 13 9 5
Testcase 2: Boundary Traversal will be 12 11 10 9 5 1 2 3 4 8.
Testcase 3: Boundary Traversal will be 1 2 3 4.
Testcase 4: Boundary Traversal will be 1 2 3 4.
'''
    Your task is to print boundary traversal
	of a given matrix.

	Function Arguments : a(given array), n (no of rows), m (no of columns).
	Return Type: none, you have to print the result.
'''

"""


def BoundaryTraversal(a, n, m):
    # code here
    perimeter = 2 * (m + n)
    pattern = [
        min(0, n - 1),  # i min
        max(0, m - 1),  # j max
        max(0, n - 1),  # i max
        min(0, m - 1)  # j min
    ]
    i, j = 0, 0
    ind = 0
    completed = []
    while ind < len(pattern):
        if ind == 0:
            for i in range(m):
                x = pattern[ind]
                y = i
                print(a[x][y], end=" ")
                completed.append([x, y])
        elif ind == 1:
            for i in range(1, n):
                x = i
                y = pattern[ind]
                if [x, y] not in completed:
                    print(a[x][y], end=" ")
                    completed.append([x, y])
        elif ind == 2:
            for i in range(m - 2, -1, -1):
                x = pattern[ind]
                y = i
                if [x, y] not in completed:
                    print(a[x][y], end=" ")
                    completed.append([x, y])
        else:
            for i in range(n - 2, 0, -1):
                x = i
                y = pattern[ind]
                if [x, y] not in completed:
                    print(a[x][y], end=" ")
                    completed.append([x, y])
        ind += 1
# {
#  Driver Code Starts
# Initial Template for Python 3
# Contributed by : Nagendra Jha

# import atexit
# import io
# import sys


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        a = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(values[k])
                k += 1
            a.append(row)
        BoundaryTraversal(a, n, m)
        print()

# } Driver Code Ends
