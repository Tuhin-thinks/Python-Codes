"""
Problem Statement:
Stickler Thief 
Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule when looting the houses. According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy. He asks for your help to find the maximum money he can get if he strictly follows the rule. Each house has a[i] amount of money present in it.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each test case contains an integer n which denotes the number of houses. Next line contains space separated numbers denoting the amount of money in each house.

Output:
For each testcase, in a newline, print an integer which denotes the maximum amount he can take home.

Expected Time Complexity: O(N).
Expected Space Complexity: O(N).

Constraints:
1 <= T <= 200
1 <= n <= 104
1 <= a[i] <= 104

Example:
Input:
2
6
5 5 10 100 10 5
3
1 2 3
Output:
110
4

Explanation:
Testcase1:
5+100+5=110
Testcase2:
1+3=4
"""

def FindMaxSum(a,n):
    if n == 0:
        return 0
    elif n == 1:
        return a[0]
    elif n == 2:
        return max(a[0],a[1])
    
    dp = []
    dp.extend([a[0],max(a[0],a[1])])
    
    for i in range(2,n):
        dp.append(max(dp[i-2]+a[i],dp[i-1]))
    
    return dp[-1]

if __name__ == '__main__':
    testcases = int(input())
    for cases in range(testcases):
        n = int(input())
        a = list(map(int,input().split()))
        print(FindMaxSum(a,n))