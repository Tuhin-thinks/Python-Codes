"""
Given two sorted arrays of distinct elements. There is only 1 difference between the arrays. First array has one element extra added in between. Find the index of the extra element.

Input:
The first line of input contains an integer T, denoting the no of test cases. Then T test cases follow. The first line of each test case contains an integer N, denoting the number of elements in array. The second line of each test case contains N space separated values of the array A[]. The Third line of each test case contains N-1 space separated values of the array B[].

Output:
Return the index (0 based indexing) of the corresponding extra element in array A[].(starting index 0).

User Task:
You don't have to take any input. Just complete the provided function findExtra() that takes array A[], B[] and size of A[] and return the valid index (0 based indexing).

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1<=T<=100
2<=N<=104
1<=Ai<=105

Example:
Input:
2
7
2 4 6 8 9 10 12
2 4 6 8 10 12
6
3 5 7 9 11 13
3 5 7 11 13
Output:
4
3

Explanation:
Testcase 1: In the second array, 9 is missing and it's index in the first array is 4.
Testcase 2: In the second array, 9 is missing and it's index in the first array is 3.
"""


def findExtra(a, b, n):
    # add code here
    # find the missing element
    if len(a) == n:  # means a is larger
        extra_element = list(set(a) - set(b))[0]
        extra_elem_index = a.index(extra_element)
        return extra_elem_index


# {
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(findExtra(a, b, n))
# } Driver Code Ends
