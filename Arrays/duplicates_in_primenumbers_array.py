"""
Given an array consisting of only prime numbers, remove all duplicate numbers from it.
Note: Retain the first occurrence of the duplicate element.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines, first of which contains N, the size of array. The second line contains N space separated elements of the array.

Output:
Print the resultant array with no duplicate elements.

Your Task:
Complete the function removeDuplicate() that takes given array and N as input parameters and returns modified array which has no duplicates.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1<=T<=200
1<=N=1000
2<=A[i]<100

Example:
Sample Input:
1
6
2 2 3 3 7 5

Sample Output:
2 3 7 5

Explanation:
After removing the duplicate 2 and 3 we get 2 3 7 5.
"""


def removeDuplicates(arr):
    # code here
    registered = []
    for i in arr:
        if i not in registered:
            registered.append(i)
    return registered


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        res = removeDuplicates(arr)
        for i in res:
            print(i, end=" ")
        print()
