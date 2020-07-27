"""
Find nth element of spiral matrix

Given a matrix your task is to find the kth element which is obtained while traversing the matrix spirally. You need to complete the method findK which takes four arguments the first argument is the matrix A and the next two arguments will be n and m denoting the size of the matrix A and then the forth argument is an integer  k denoting the kth element . The function will return the kth element obtained while traversing the matrix spirally.


Input:
The first line of input is the no of test cases then T test cases follow . The first line of each test case has three integers n(rows), m(columns) and k . Then in the next line are n*m space separated values of the matrix A [ ] [ ] .

Output:
The output for each test case will be the kth obtained element .

Your Task:
You only need to implement the given function findK(). Do not read input, instead use the arguments given in the function. Return the K'th element obtained by traversing matrix spirally.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)



Constraints:
1<=T<=100
1<=n,m<=20
1<=k<=n*m

Example:
Input
1
3 3 4
1 2 3 4 5 6 7 8 9

Output
6

Explanation
The matrix above will look like
1 2 3
4 5 6
7 8 9
and the 4th element in spiral fashion will be 6 .

Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
"""


# Function should return the an integer
def findK(arr, m, n, q):
    # Code here
    elements = m * n
    top, down, left, right = 0, m - 1, 0, n - 1
    count = 0
    direction = 0

    while count < elements:
        if direction == 0:
            for i in range(left, right + 1):
                # print(arr[top][i], end=" ")
                count += 1
                if count == q:
                    return arr[top][i]
            top += 1
            direction = 1
        elif direction == 1:
            for i in range(top, down + 1):
                # print(arr[i][right], end=" ")
                count += 1
                if count == q:
                    return arr[i][right]
            direction = 2
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                # print(arr[down][i], end=" ")
                count += 1
                if count == q:
                    return arr[down][i]
            direction = 3
            down -= 1
        elif direction == 3:
            for i in range(down, top - 1, -1):
                # print(arr[i][left], end=" ")
                count += 1
                if count == q:
                    return arr[i][left]
            left += 1
            direction = 0


# {
#  Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])] for j in range(n[0])]
        c = 0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c += 1
        print(findK(matrix, n[0], n[1], n[2]))
# } Driver Code Ends
