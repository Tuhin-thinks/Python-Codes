"""
Search in a row-column sorted Matrix

Given a matrix mat[] of size n x m, where every row and column is sorted in increasing order, and a number x is given. The task is to find whether element x is present in the matrix or not.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consists of three lines. First line of each test case consist of two space separated integers N and M, denoting the number of element in a row and column respectively. Second line of each test case consists of N*M space separated integers denoting the elements in the matrix in row major order. Third line of each test case contains a single integer x, the element to be searched.

Output:
Corresponding to each test case, print in a new line, 1 if the element x is present in the matrix, otherwise simply print 0.

Your Task:
This is a function problem. You only need to complete the function search that takes n,m, and x as parameters and returns either 0 or 1.

Expected Time Complexity: O(N + M)
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 200
1 <= N, M <= 1000
1 <= mat[][] <= 105
1 <= X <= 1000

Example:
Input:
2
3 3
3 30 38 44 52 54 57 60 69
62
1 6
18 21 27 38 55 67
55
Output:
0
1

Explanation:
Testcase 1: 62 is not present in the matrix, so output is 0.
Testcase 2: 55 is present in the matrix at 5th cell.
"""

def search(n1, m1, mat, x):
    i, j = 0, m1 - 1
    while True:
        if 0 <= i < n1 and 0 <= j < m1:
            elem = mat[i][j]
            if elem == x:
                return 1
            elif elem < x:
                i += 1
            elif elem > x:
                j -= 1
        else:
            break
    return 0


def main():
    T = int(input())
    while T > 0:
        n, m = map(int, input().split())
        mat = [[0 for j in range(m)] for i in range(n)]
        line_1 = [int(x) for x in input().strip().split()]
        x = int(input())

        k = 0
        for i in range(n):
            for j in range(m):
                mat[i][j] = line_1[k]
                k += 1
        print(search(n, m, mat, x))
        T -= 1


if __name__ == '__main__':
    main()
