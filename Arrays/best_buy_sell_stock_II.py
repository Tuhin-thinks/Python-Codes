# Problem source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        buy = prices[0]
        profit = 0
        i = 0

        while i < len(prices):
            price = prices[i]

            if price < prices[i - 1]:
                # sell the stock and update the buy price
                profit += prices[i - 1] - buy
                buy = price

        # no need to keep check, since when there's no peak, buy will be same as last price
        profit += prices[-1] - buy  # evaluates to 0 when there's no peak

        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    res = sol.maxProfit(prices)
    print(res)
