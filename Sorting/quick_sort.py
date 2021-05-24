"""
Problem Statement:
Quick Sort

Given an array of integers. Complete the partition() function used for the implementation of Quick Sort.

Example 1:

Input: N = 5, arr[] = { 4, 1, 3, 9, 7}
Output: 1 3 4 7 9

Example 2:

Input: N = 10,
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 1 2 3 4 5 6 7 8 9 10


Your Task: You don't need to read input or print anything. Your task is to complete the function partition() which takes the array arr[] and the range of indices to be considered [low, high] and partitions the array in the given range considering the last element as the pivot such that, all the elements less than(or equal to) the pivot lie before the elements greater than it.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 103
1 <= arr[i] <= 104
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        quicksort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
