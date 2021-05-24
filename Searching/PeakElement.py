"""
Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.
Note: There may be multiple peak element possible, in that case you may return any valid index (0 based indexing).

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N. Then in the next line are N space separated values of the array.

Output:
For each test case output will be 1 if the index returned by the function is an index with peak element.

User Task:
You don't have to take any input. Just complete the provided function peakElement() and return the valid index.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[] <= 106

Example:
Input:
2
3
1 2 3
2
3 4
Output:
1
1

Explanation:
Testcase 1: In the given array, 3 is the peak element as it is greater than its neighbour.
Testcase 2: 4 is the peak element as it is greater than its neighbour elements.
"""


# function should return index to the any valid peak element
def peakElement(arr, n):
    # Code here
    i = 0
    while i < n:
        if i != 0 and i != n - 1:
            left_neighbour = arr[i - 1]
            right_neighbour = arr[i + 1]
            element = arr[i]
            if element > left_neighbour and element > right_neighbour:
                return i
        elif i == 0:
            if n > 1:
                right_neighbour = arr[i + 1]
                element = arr[i]
                if element > right_neighbour:
                    return i
            else:
                return 0
        elif i == n - 1:
            left_neighbour = arr[i - 1]
            element = arr[i]
            if element > left_neighbour:
                return i
        i += 1


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = peakElement(arr, n)
        flag = False
        if index == 0 and n == 1:
            flag = True
        elif index == 0 and arr[index] >= arr[index + 1]:
            flag = True
        elif index == n - 1 and arr[index] >= arr[index - 1]:
            flag = True
        elif arr[index - 1] <= arr[index] and arr[index] >= arr[index + 1]:
            flag = True
        else:
            flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
