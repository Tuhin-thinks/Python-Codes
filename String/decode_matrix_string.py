"""
HackerRank problem link: https://www.hackerrank.com/challenges/matrix-script/problem
"""
import re

def column_traversal_string(matrix):
    string = ""
    for i in matrix:
        for j in i:
            string += j
    return string

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

entered_string = column_traversal_string(matrix)
res = re.sub(r"\w()\w")