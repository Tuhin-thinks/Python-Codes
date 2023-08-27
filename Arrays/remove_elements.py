# Problem source: https://leetcode.com/problems/remove-element/submissions/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_length = len(nums)
        current_index = 0
        insert_index = 0

        while current_index < len(nums):
            el = nums[current_index]

            if el == val:
                new_length -= 1

            elif current_index != insert_index:
                # replace elements
                nums[insert_index] = nums[current_index]
                insert_index += 1
            else:
                insert_index += 1

            current_index += 1

        return new_length
