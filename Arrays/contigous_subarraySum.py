import math

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        max_so_far = -10**7
        max_end_here = 0

        for i in range(size):
            max_end_here += a[i]
            if max_so_far < max_end_here:
                max_so_far = max_end_here
            if max_end_here < 0:
                max_end_here = 0
        return max_so_far

def main():
    T = int(input())
    while T > 0:
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxSubArraySum(arr, n))

        T -= 1


if __name__ == '__main__':
    main()