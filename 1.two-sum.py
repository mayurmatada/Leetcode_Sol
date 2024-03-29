#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = nums.copy()
        sorted_nums.sort()
        i = 0
        j = len(nums)-1
        while (sorted_nums[i]+sorted_nums[j] != target):
            if (target > sorted_nums[i]+sorted_nums[j]):
                i += 1
            else:
                j -= 1
        index_a = nums.index(sorted_nums[i])
        if (sorted_nums[i] == sorted_nums[j]):
            nums.remove(sorted_nums[i])
            index_b = nums.index(sorted_nums[j])+1
        else:
            index_b = nums.index(sorted_nums[j])
        return [index_a, index_b]


# @lc code=end
