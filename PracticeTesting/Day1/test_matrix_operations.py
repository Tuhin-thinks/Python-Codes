# use pytest to test various matrix operations
from pytest import fixture, raises

import script


@fixture
def matrix():
    matrix_ = [
        [1, 0, 1],
        [-1, 1, 1],
        [0, 1, 0]
    ]
    return matrix_


def test_get_determinant(matrix):
    assert script.get_determinant(matrix) == -2


def test_get_minor(matrix):
    assert script.get_minor(matrix, 0, 0) == [[1, 1], [1, 0]]
    assert script.get_minor(matrix, 0, 1) == [[-1, 1], [0, 0]]

    assert script.get_minor(matrix, 1, 1) == [[1, 1], [0, 0]]
    assert script.get_minor(matrix, 2, 2) == [[1, 0], [-1, 1]]


def test_transpose_matrix(matrix):
    transposed_matrix = [
        [1, -1, 0],
        [0, 1, 1],
        [1, 1, 0]
    ]
    assert transposed_matrix == script.transpose_matrix(matrix)


def test_inverse_matrix(matrix):
    inverse_matrix = [
        [1/2, -1/2, 1/2],
        [0, 0, 1],
        [1/2, 1/2, -1/2]
    ]
    assert inverse_matrix == script.inverse_matrix(matrix)

    singular_matrix = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    with raises(ValueError) as ex:
        script.inverse_matrix(singular_matrix)
        # check exception message
        assert str(ex.value) == 'The matrix is not invertible. The determinant is 0.'
