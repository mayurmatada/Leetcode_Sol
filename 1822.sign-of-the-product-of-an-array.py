#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = True
        for i in nums:
            if (i < 0):
                sign = not sign
            elif (i == 0):
                return 0
        return 1 if sign is True else -1

# @lc code=end
