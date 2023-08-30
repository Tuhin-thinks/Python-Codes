# Problem source: https://leetcode.com/problems/jump-game/submissions/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        index = l - 1
        temp_index = index

        for index in range(l - 1, -1, -1):
            el = nums[index]

            if index + el >= temp_index:
                temp_index = index

        return temp_index == 0
