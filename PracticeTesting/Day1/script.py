def get_minor(matrix: list, row: int, col: int) -> list:
    """
    Get the minor of a matrix.

    :param matrix: The matrix to get the minor of.
    :param row: The row of the minor.
    :param col: The column of the minor.
    :return: The minor of the matrix.
    """
    n = len(matrix)
    minor = []
    for i in range(n):
        _row = []
        if i != row:
            for j in range(n):
                if j != col:
                    _row.append(matrix[i][j])
            minor.append(_row)

    return minor


def get_determinant(matrix: list) -> float:
    """
    Get the determinant of a matrix.

    :param matrix: The matrix to get the determinant of.
    :return: The determinant of the matrix.
    """
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0

    # iterate through the first row
    for i in range(n):
        minor = get_minor(matrix, 0, i)
        determinant += matrix[0][i] * (-1) ** i * get_determinant(minor)
    return determinant


def transpose_matrix(matrix: list) -> list:
    """
    Transpose a matrix.

    :param matrix: The matrix to transpose.
    :return: The transpose matrix.
    """
    n = len(matrix)
    transpose = []
    for i in range(n):
        _row = []
        for j in range(n):
            _row.append(matrix[j][i])
        transpose.append(_row)
    return transpose


def inverse_matrix(matrix: list) -> list:
    """
    Inverse a matrix.

    :param matrix: The matrix to inverse.
    :return: The inverse matrix.
    """
    n = len(matrix)
    determinant = get_determinant(matrix)
    if determinant == 0:
        raise ValueError("The matrix is not invertible. The determinant is 0.")
    inverse = []
    for i in range(n):
        _row = []
        for j in range(n):
            minor = get_minor(matrix, i, j)
            minor_determinant = get_determinant(minor)
            A_ij = (-1) ** (i + j) * minor_determinant
            _row.append(A_ij / determinant)
        inverse.append(_row)
    return transpose_matrix(inverse)
