#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


def binsearch(nums: List[int], index: int, target: int) -> int:
    if (len(nums) == 1):
        return index if nums[0] == target else -1
    else:
        if (nums[int(len(nums)/2)] == target):
            return int(len(nums)/2)+index
        elif (nums[int(len(nums)/2)] < target):
            return binsearch(nums[int(len(nums)/2):], index+int(len(nums)/2), target=target)
        elif (nums[int(len(nums)/2)] > target):
            return binsearch(nums[:int(len(nums)/2)], index, target=target)
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binsearch(nums=nums, index=0, target=target)


# @lc code=end
