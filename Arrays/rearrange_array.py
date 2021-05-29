"""
Problem statement:
Rearrange an array with O(1) extra space

Given an array arr[] of size N where every element is in the range from 0 to n-1. Rearrange the given array so that arr[i] becomes arr[arr[i]].

Example 1:

Input:
N = 2
arr[] = {1,0}
Output: 0 1
Explanation: arr[0] = 1 and arr[arr[0]]
= 0.Also, arr[1] = 0 and arr[arr[1]] = 1.
So, rearranging elements, we get array 
as, 0 1.

Example 2:

Input:
N = 5
arr[] = {4,0,2,1,3}
Output: 3 4 2 0 1
Explanation: arr[0] = 4 and arr[arr[0]] 
= 3. Also, arr[1] = 0 and arr[arr[1]] 
= 4 and so on. So, rearranging elements,
we get array as 3 4 2 0 1.

Your Task:
The task is to complete the function arrange() which arranges the elements in the array. The printing is done automatically done by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 107
0 <= Arr[i] < N
"""

def arrange(arr, n): 
    #Your code here
    new_arr = arr.copy()
    i = 0
    while i<n:
        elem = new_arr[i]
        arr[i] = new_arr[elem]
        i += 1

if __name__ == "__main__":
    t = int(input())
    
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        arrange(arr,n)
        for i in arr:
            print(i,end=" ")
        print()
        t -= 1

