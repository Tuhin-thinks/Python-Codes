"""
source: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
"""
class Solution:
    def sort012(self,arr,n):
        # code here
        elem_hash = {}
        for elem in arr:
            if elem in elem_hash:
                elem_hash[elem] += 1
            else:
                elem_hash[elem] = 1
        arr.clear()
        for elem in elem_hash.keys():
            arr.extend([elem]*elem_hash[elem])

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=" ")
        print()