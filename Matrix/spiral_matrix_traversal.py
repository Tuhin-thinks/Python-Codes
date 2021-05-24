"""Spirally traversing a matrix
Given a matrix mat[][] of size M*N. Traverse and print the matrix in spiral form.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test cases follow. Each testcase has 2 lines. First line contains M and N respectively separated by a space. Second line contains M*N values separated by spaces.

Output:
Elements when traveled in Spiral form, will be displayed in a single line.

Your Task:
This is a function problem. You only need to complete the function spirallyTraverse that takes m, n, and matrix as parameters and prints the spiral traversal. The driver code automatically appends a new line.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 100
2 <= M, N <= 100
0 <= Ai <= 100

Example:
Input:
2
4 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4
1 2 3 4 5 6 7 8 9 10 11 12
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
1 2 3 4 8 12 11 10 9 5 6 7

Explanation:
Testcase 1:


Testcase 2: Applying same technique as shown above , output for the 2nd testcase will be 1 2 3 4 8 12 11 10 9 5 6 7."""

# Complete this function
# a is the matrix
# m is rows
# n is cols
def spirallyTraverse(m, n, a):
    # Your code here
    elements = m * n
    top, down, left, right = 0, m - 1, 0, n - 1
    count = 0
    direction = 0

    while count < elements:
        if direction == 0:
            for i in range(left, right + 1):
                print(a[top][i], end=" ")
                count += 1
            top += 1
            direction = 1
        elif direction == 1:
            for i in range(top, down + 1):
                print(a[i][right], end=" ")
                count += 1
            direction = 2
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                print(a[down][i], end=" ")
                count += 1
            direction = 3
            down -= 1
        elif direction == 3:
            for i in range(down, top - 1, -1):
                print(a[i][left], end=" ")
                count += 1
            left += 1
            direction = 0


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while (T > 0):
        n, m = map(int, input().split())
        mat = [[0 for j in range(m)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]

        k = 0
        for i in range(n):
            for j in range(m):
                mat[i][j] = line1[k]
                k += 1

        k = 0

        n, m = m, n

        spirallyTraverse(m, n, mat)

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
