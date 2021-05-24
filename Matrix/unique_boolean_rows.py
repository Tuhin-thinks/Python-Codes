"""
Unique rows in boolean matrix

Given a binary matrix your task is to complete the function printMat which prints all unique rows of the given matrix. The function takes three arguments the first argument is a matrix M and the next two arguments are row and col denoting the rows and columns of the matrix.

Input:
The first line of input is an integer T denoting the no of test cases. Then T test cases follow. Each test case consists of 2 lines. The first line of each test contains two integers row and col denoting the number of rows and columns of matrix. Then in the next line are row*col space separated values of the matrix M.

Output:
The output will be the unique rows of the matrix separated by space.

Note: The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

Note : Dont print new line after each row instead print "$" without quotes.

Your Task:
You only need to implement the given function printMat(). Do not read input, instead use the arguments given in the function.

Expected Time Complexity: O(row * col)
Expected Auxiliary Space: O(row * col)

Constraints:
1<=T<=20
1<=row,col<=40
0<=M[][]<=1

Example:
Input
1
3 4
1 1 0 1 1 0 0 1 1 1 0 1

Output
1 1 0 1 $1 0 0 1 $

Explanation
Above the matrix of size 3x4 looks like
1 1 0 1
1 0 0 1
1 1 0 1
The two unique rows are 1 1 0 1 and 1 0 0 1 .
** For More Input/Output Examples Use 'Expected Output' option **
"""


def printmat(row, col, matrix):
    new_matrix = []
    new_matrix = [matrix[i:i + col] for i in range(0, len(matrix), col)]
    # print(new_matrix)
    unique = []
    for r in new_matrix:
        if r not in unique:
            unique.append(r)
            print(' '.join(r), end=' $')
    print()


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    testcase = int(input())
    while (testcase):
        s = input().split()
        row = int(s[0])
        col = int(s[1])
        matrix = input().split()

        printmat(row, col, matrix)

        testcase -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
