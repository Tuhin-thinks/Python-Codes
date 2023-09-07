# Problem source: https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # variable storing the required answer
        n_jumps = 0

        # 2 pointers
        start = 0
        end = 0

        while end < len(nums) - 1:
            max_jump_possible = 0

            for i in range(start, end + 1):
                max_jump_possible = max(max_jump_possible, i + nums[i])

            # update the pointers
            start = end + 1
            end = max_jump_possible

            # update the number of jumps
            n_jumps += 1

        return n_jumps
