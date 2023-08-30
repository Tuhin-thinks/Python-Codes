# Problem source: https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el = 0
        count = 0

        for i in range(len(nums)):
            if count == 0:
                el = nums[i]
                count += 1
            elif el == nums[i]:
                count += 1
            else:
                count -= 1

        return el


if __name__ == '__main__':
    nums = [3, 3, 4]
    sol = Solution()
    res = sol.majorityElement(nums)
    print(res)
