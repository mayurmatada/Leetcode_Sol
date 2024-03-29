#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        no_of_zeroes = nums.count(0)
        cur = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[cur] = nums[i]
                cur += 1
        for i in range(len(nums)-1, len(nums)-no_of_zeroes-1, -1):
            nums[i] = 0

# @lc code=end
