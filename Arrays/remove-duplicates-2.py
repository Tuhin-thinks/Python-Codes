# Problem source: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nd = {}

        i = 0  # index pointer
        j = 0  # replace pointer
        k = len(nums)

        while i < len(nums):
            el = nums[i]

            if nd.get(el, 0) >= 2:
                k -= 1
                nd[el] += 1  # increase the number's count
            else:
                val = nd.setdefault(el, 0)
                nd[el] += 1

                if j != i:
                    nums[j] = el

                j += 1  # increase the replace pointer

            i += 1

        return k
