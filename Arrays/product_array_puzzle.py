
"""
Problem statement:
Given an array A of size N, construct a Product Array P (of same size) such that P is equal to the product of all the elements of A except A[i].

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line is N. The second line contains N elements separated by spaces. It is guranteed that the product of all the elements of the array will not exceed 1e18.

Output:
For every test case, print the product array in a new line. If the array has only one element print 1. 

Your Task:
You do not have to read input. Your task is to complete productExceptSelf() function and returns the Product vector P that holds product except for self at each index.

Note: Try to solve this problem without using the division operation.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 100
1 <= N <= 1000
0 <= Ai <= 200

Example:
Input:
2
5
10 3 5 6 2
2
12 0
Output:
180 600 360 300 900
0 12

Explanation:
Testcase1: For the product array P, at i=0 we have 3*5*6*2. At i=1 10*5*6*2. At i=2 we have 10*3*6*2. At i=3 we have 10*3*5*2. At i=4 we have 10*3*5*6
So P is 180 600 360 300 900
 
"""
def productExceptSelf(arr, n):
    #code here
    p = []
    prod = 1
    flag = 0
    for i in arr:
        if i != 0:
            prod *= i
        else:
            flag += 1
        
    for i in arr:
        if flag > 1:
            p.append(0)
        else:
            if i != 0 and flag == 1:
                p.append(0)
            elif i == 0 and flag == 1:
                p.append(prod)
            else:
                p.append(prod//i)
    return p
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends