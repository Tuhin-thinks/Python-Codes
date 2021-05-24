"""
Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N. Find the missing element.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case first line contains N denoting the size of the array. The subsequent line contains N-1 space separated array elements.

Output:
Print the missing number.

Your Task :
Complete the function MissingNumber() that takes array and N as input and returns the value of the missing number.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 106
1 ≤ array[i] ≤ 106

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
Testcase 2: Given array : 1 2 3 4 5 6 7 8 10. Missing element is 9
"""

def MissingNumber(array,n):
    # code here
    array_sum = sum(array)
    expected = int((n / 2) * (2 + n - 1))
    # print(f'Array sum:{array_sum}, expected:{expected}')
    missing_element = int(expected) - array_sum
    return missing_element


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = MissingNumber(a, n)
    print(s)