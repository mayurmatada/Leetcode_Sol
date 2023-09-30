#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        i = 0
        j = len(nums)-1
        flag = False
        cpy = nums.copy()
        cpy.sort()
        while(flag == False):
            if(nums[i] + nums[j] < target):
                i = i+1
            elif(nums[i] + nums[j] > target):
                j = j-1
            if(nums[i] + nums[j]  == target):
                result.append(nums.index(cpy[i]))
                result.append(nums.index(cpy[j]))
        return result


# @lc code=end

