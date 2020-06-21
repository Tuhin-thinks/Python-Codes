"""
Given two sorted arrays A and B, such that the arrays may have some common elements. Find the sum of the maximum sum path to reach from the beginning of any array to end of any of the two arrays. We can switch from one array to another array only at the common elements.

Input:
First line of input contains number of testcases T. For each testcase, there will be three lines. First line contains M and N denoting the length of the two sorted array A and B respectively. Second line contains elements of array A. Third line contains elements of array B.

Output:
For each test case, the output is the max sum obtained from the two arrays.

Your Task:
Complete the function max_path_sum() that takes the two arrays A and B along with their sizes M and N as input parameters. It returns the sum of the maximum sum path.

Expected Time Complexity: O(M + N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 100
1 <= M,N <= 105
1 <= A[i], B[i] <= 106

Example:
Sample Input:
2
5 4
2 3 7 10 12
1 5 7 8
3 3
1 2 4
1 2 7

Sample Output:
35
10

Explanation:
Testcase 1: The path will be 1+5+7+10+12 = 35.
Testcase 2: The path will be 1+2+7=10
"""
def maxSumPath(arr1, arr2, m, n):
    # code here
    # 1 2 3 5 6
    # 2 3 3 4
    sum1 = 0
    sum2 = 0
    i = 0
    j = 0
    mainsum = 0
    while i < m and j < n:

        if arr1[i] == arr2[j]:
            mainsum += max(sum1, sum2)
            # print("mainsum incremented ",mainsum)
            sum1 = arr1[i]
            sum2 = arr2[j]
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        elif arr2[j] < arr1[i]:
            sum2 += arr2[j]
            j += 1

    for num in arr2[j:]:
        sum2 += num
    for num in arr1[i:]:
        sum1 += num
    # print(sum1,sum2)
    mainsum += max(sum1, sum2)

    return (mainsum)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m,n = list(map(int, input().split()))
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        print(maxSumPath(arr1, arr2, m, n))