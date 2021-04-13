"""
source:https://leetcode.com/problems/next-permutation/
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:   # nums are in descending order
            nums.reverse()
            return   # usinf return statement to end the execution here (use the reversed nums array)


        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1  # reverse the second part

        # loop to reverse from next ascending element to end of array (inplace)
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1


def main():
    tc = int(input())
    while tc:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.nextPermutation(arr)  # inplace modification
        print(arr)
        tc -= 1

if __name__ == '__main__':
    main()
