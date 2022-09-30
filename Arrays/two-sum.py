"""
Problem link: https://leetcode.com/problems/two-sum/
"""

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i1, e1 in enumerate(nums):
    #         for i2, e2 in enumerate(nums):
    #             if i2 != i1 and e1 + e2 == target:
    #                 return [i1, i2]
    # ---------------- another way --------------------
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []
