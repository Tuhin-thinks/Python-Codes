"""
Problem Statement:
Union of Two Sorted Arrays

Given two sorted arrays arr[] and brr[] of size N and M respectively. The task is to find the union of these two arrays.
Union of two arrays can be defined as the common and distinct elements in the two arrays.

Example 1:

Input: 
N = 5, arr1[] = {1, 2, 3, 4, 5}  
M = 3, arr2 [] = {1, 2, 3}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.

Example 2:

Input: 
N = 5, arr1[] = {2, 2, 3, 4, 5}  
M = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.

Example 3:

Input:
N = 5, arr1[] = {1, 1, 1, 1, 1}
M = 5, arr2[] = {2, 2, 2, 2, 2}
Output: 1 2
Explanation: Distinct elements including 
both the arrays are: 1 2.


Your Task: This is a function problem. You only need to complete the function findUnion() that takes two arrays arr1[], arr2[], and their size N and M as parameters and returns the union of two arrays. The new line is automatically appended by the driver code.

Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(N+M).

Constraints:
1 <= N, M <= 105
1 <= arr[i], brr[i] <= 106
"""
def mergeArrays(a,b,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    '''
    # code here 
    union_array = a+b
    sorted_union_array = list(set(union_array))
    return sorted(sorted_union_array)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        li = mergeArrays(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends