"""
Problem Statement:
Missing number in array
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9

Explanation:
Testcase 1: Given array : 1 2 3 5. Missing element is 4.
"""

if __name__=='__main__':
    test_cases=int(input())  # number of test cases
    for i in range(test_cases):
        number_of_elements = int(input())  # number of array elements to add
        elements = list(map(int, input().split()))
        predicted_elements = set()
        for j in range(1, number_of_elements+1, 1):
            predicted_elements.add(j)
        diff_set = predicted_elements - set(elements)  # find the missing element by subtracting
        for missing_element in diff_set:
            print(missing_element)
