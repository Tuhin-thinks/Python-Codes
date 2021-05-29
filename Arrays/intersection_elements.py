"""
Intersection of two arrays

Given two arrays A and B respectively of size N and M, the task is to print the count of elements in the intersection (or common elements) of the two arrays.

For this question, the intersection of two arrays can be defined as the set containing distinct common elements between the two arrays. 

Example 1:

Input:
N = 5, M = 3
A[] = {89,24,75,11,23}
B[] = {89,2,4}
Output: 1
Explanation: 89 is the only element 
in the intersection of two arrays.

Example 2:

Input:
N = 6, M = 5
A[] = {1,2,3,4,5,6}
B[] = {3,4,5,6,7}
Output: 4
Explanation: 3 4 5 and 6 are the elements 
in the intersection of two arrays.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N and M, N is the size of array A and M is the size of array B. The second line of each test case contains N input A[i].
The third line of each test case contains M input B[i].

Output:
Print the count of intersecting elements.

Your Task:
The task is to complete the function NumberofElementsInIntersection() which takes 4 inputs ie- array a, array b, n which is the size of array a, m which is the size of array b. The function should return the count of the number of elements in the intersection.

Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(min(N,M)).

Constraints:
1 ≤ N, M ≤ 105
1 ≤ A[i], B[i] ≤ 105

Time limit: 30 min
Code has expected 0.03s time complexity
"""


def NumberofElementsInIntersection(a, b, n, m):
    return len(set.intersection(set(a),set(b)))


#{ 
#  Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]