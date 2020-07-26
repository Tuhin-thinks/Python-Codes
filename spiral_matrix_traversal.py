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
