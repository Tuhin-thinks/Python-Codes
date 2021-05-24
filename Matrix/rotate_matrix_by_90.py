"""Given a square matrix[][] of size N x N. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case consists of an integer N, where N is the size of the square matrix. The second line of each test case contains N x N space-separated values of the matrix.

Output:
Corresponding to each test case, in a new line, print the rotated array.

Your Task:
You only need to implement the given function rotate(). Do not read input, instead use the arguments given in the function.

Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 50
1 <= matrix[][] <= 100

Example:
Input:
1
3
1 2 3 4 5 6 7 8 9
Output:
3 6 9
2 5 8
1 4 7

 """


def rotate(matrix):
    # code here
    arr = []
    for i in matrix:
        arr.extend(i)
    n = len(matrix)
    j = n - 1
    x = 0
    y = 0
    while j >= 0:
        k = j
        while k < len(arr):
            matrix[x][y] = arr[k]
            k = k + n
            y += 1
        j = j - 1
        x += 1
        y = 0


# { 
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = [int(x) for x in input().split()]
        matrix = []

        for i in range(0, N * N, N):
            matrix.append(arr[i:i + N])

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()

# } Driver Code Ends
