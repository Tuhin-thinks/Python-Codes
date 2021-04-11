"""
source: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1
"""
def merge(arr1, m, arr2, n):
    tot_size = m + n
    gap = tot_size // 2 + tot_size % 2
    for i in range(tot_size):
        if i < m:
            a = arr1[i]
