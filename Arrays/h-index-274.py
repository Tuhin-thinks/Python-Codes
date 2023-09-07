# Problem source: https://leetcode.com/problems/h-index/description/
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        l = len(citations)
        h = 0

        for i in range(l):
            if citations[i] >= i + 1:
                h = i + 1

        return h
