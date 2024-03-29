#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        low = 0
        high = 1
        while (high < len(prices)):
            if prices[low] < prices[high]:
                profit = prices[high] - prices[low]
                maxprofit = max(profit, maxprofit)
            else:
                low = high
            high += 1
        return maxprofit


# @lc code=end
