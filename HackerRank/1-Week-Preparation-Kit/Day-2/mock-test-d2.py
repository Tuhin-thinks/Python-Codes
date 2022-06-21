def flippingMatrix(matrix):
    half_length = len(matrix) // 2
    max_sum = 0
    # iterate in the top left quadrant of the matrix

    for i in range(half_length):
        # iterate in the top left quadrant of the matrix
        for j in range(half_length):
            max_sum += max(
                max(matrix[i][j], matrix[i][2*half_length-1-j]),
                max(matrix[2*half_length-1-i][j], matrix[2*half_length-1-i][2*half_length-1-j])
            )

    return max_sum


if __name__ == '__main__':
    fptr = open("../output.txt", 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
