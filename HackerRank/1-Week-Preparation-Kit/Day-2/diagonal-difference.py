def diagonalDifference(arr):
    left_diagonal_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == j:
                left_diagonal_sum += arr[i][j]
                break

    right_diagonal_sum = 0
    for row in range(len(arr)):
        for col in range(len(arr) - 1, -1, -1):
            if row == len(arr) - col - 1:
                right_diagonal_sum += arr[row][col]
    return abs(right_diagonal_sum - left_diagonal_sum)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    result = diagonalDifference(arr)
    print(result)
