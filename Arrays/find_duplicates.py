"""
Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N which denotes the number of elements in the array. The second line of each test case contains n space separated integers denoting elements of the array a[].

Output:
Print the duplicate elements from the given array. The order of the output should be in sorted order. Print -1 if no duplicate exists.

Your Task:
Complete the function duplicates() which takes array a[] and n as input as parameters and returns a list of elements that occur more than once in the given array in sorted manner. If no such element is found return -1.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
Note : The extra space is only for the array to be returned.
Try and perform all operation withing the provided array.

Constraints:
1 <= T <= 100
1 <= N <= 105
0 <= A[i] <= N-1, for each valid i

Example:
Sample Input:
2
4
0 3 1 2
5
2 3 1 2 3

Sample Output:
-1
2 3

Explanation:
Testcase 1: N=4 and all elements from 0 to (N-1 = 3) are present in the given array. Therefore output is -1.
Testcase 2: 2 and 3 occur more than once in the given array.
"""
def duplicates(arr, n):
    freq_dict = {}
    for i in arr:
        if i not in freq_dict.keys():
            freq_dict[i] = 1
        else:
            freq_dict[i] += 1
    res = [i for i in freq_dict.keys() if freq_dict[i] > 1]

    if len(res) == 0:
        return [-1]
    else:
        return sorted(res)

# {
#  Driver Code Starts
if (__name__ == '__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = duplicates(arr, n)
        for i in res:
            print(i, end=" ")
        print()

# } Driver Code Ends