"""source:https://leetcode.com/problems/find-the-duplicate-number/
"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for idx in range(len(nums)):
            if nums[idx] in visited:
                return nums[idx]
            else:
                visited.add(nums[idx])
        return 0