"""
Mountain Subarray Problem 
We are given an array of integers and a range, we need to find whether the subarray which falls in this range has values in the form of a mountain or not. All values of the subarray are said to be in the form of a mountain if either all values are increasing or decreasing or first increasing and then decreasing. More formally a subarray [a1, a2, a3 … aN] is said to be in form of a mountain if there exists an integer K, 1 <= K <= N such that,
a1 <= a2 <= a3 .. <= aK >= a(K+1) >= a(K+2) …. >= aN
You have to process Q queries. In each query you are given two integer L and R, denoting starting and last index of the subarrays respectively.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the array. The following line contains N space-separated integers forming the array. Next line contains an integer Q, denoting the number of queries. For each query, you are given two space-separated integers L and R in a new line. 

Output:
For each query, print "Yes" (without quotes) if the subarray is in mountain form, otherwise print "No" (without quotes) in a new line.

Expected Time Complexity: O(N + Q).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 100
1 <= N, Q <= 105
1 <= a[i] <= 106, for each valid i
0 <= L <= R <= N-1

Example:
Input:
1
8
2 3 2 4 4 6 3 2
2
0 2
1 3

Output:
Yes
No

Explanation:
For L = 0 and R = 2, a0 = 2, a1 = 3 and a2 = 2, since they are in the valid order,answer is Yes.
For L = 1 and R = 3, a1 = 3, a2 = 2 and a3 = 4, since a1 > a2 and a2 < a4 the order isn't valid, hence the answer is No.
"""
def processqueries(arr,n,m,q):
    result = []
    for i in range(m):  # each list inside q
        boundary = q[i]
        bound_a = boundary[0]
        bound_b = boundary[1]
        
        sub_array = arr[bound_a:bound_b+1]
        m = sub_array.index(max(sub_array))
        if sorted(sub_array) == sub_array:  # increasing order
            result.append('Yes')
        elif sorted(sub_array, reverse=True) == sub_array:  # decreasing order
            result.append('Yes')
        elif 0 <= m < len(sub_array):  # first increaing then decreasing
            left = sub_array[:m]
            right = sub_array[m:]
            if sorted(left) == left and sorted(right, reverse=True) == right:
                print(f"left={left}\nright={right},\nm={m},\nsub_array={sub_array}")
                result.append("Yes")
            else:
                print(f"\nLeft sub_array:{left}, \nright sub_array:{right}\nPrinting No")
                result.append("No")
    return result


if __name__ == "__main__":
    t = int(input())
    x = 0
    while x < t:
        n = int(input())
        arr = list(map(int, input().split()))
        m = int(input())
        q = list()
        for i in range(0,m):
            q.append(list(map(int, input().split())))
        result = processqueries(arr,n,m,q)
        for i in result:
            print(i)
        x += 1