"""
In information theory, linguistics and computer science, the Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. It is named after the Soviet mathematician Vladimir Levenshtein, who considered this distance in 1965.[1]

Levenshtein distance may also be referred to as edit distance, although that term may also denote a larger family of distance metrics known collectively as edit distance.[2]:32 It is closely related to pairwise string alignments.

(source: wikipedia)
"""
import pprint


def lev_distance(i, j, matrix, a, b, noted):
    if [i, j] in noted:
        return matrix[i][j]
    else:
        noted.append([i, j])
        if min(i, j) != 0:
            x = lev_distance(i - 1, j, matrix, a, b, noted) + 1
            y = lev_distance(i, j - 1, matrix, a, b, noted) + 1
            conditional_addition = (1 if a[i - 1] != b[j - 1] else 0)
            z = lev_distance(i - 1, j - 1, matrix, a, b, noted) + conditional_addition
            value = min(x, y, z)
            matrix[i][j] = value
            return value
        else:
            value = max(i, j)
            matrix[i][j] = value
            return value


def LevenshteinDistance(m, n, a, b, matrix, noted, print_perm):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            value = lev_distance(i, j, matrix, a, b, noted)
            if print_perm:
                print(f"value for lev({i},{j})={value}.")
            matrix[i][j] = value
    if print_perm:
        print('Final Matrix:')
        pprint.PrettyPrinter(indent=5).pprint(matrix)
    return matrix[m][n]


def generate_matrix(m, n,print_perm):
    matrix = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(0)
        matrix.append(temp)
    if print_perm:
        print("Matrix generated...")
        pprint.PrettyPrinter(indent=5).pprint(matrix)
    return matrix


if __name__ == '__main__':
    a = input('Word-1:')
    b = input('Word-2:')
    m, n = len(a), len(b)
    res = input("Want to see the steps:(y/n)")
    if res.lower().startswith('y'):
        print_perm = True
    else:
        print_perm = False
    matrix = generate_matrix(m + 1, n + 1,print_perm)
    distance = LevenshteinDistance(m, n, a, b, matrix, [], print_perm=print_perm)
    print(f"Word's Levenshtein Distance={distance}")
