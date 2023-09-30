#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        n = len(nums)
        index = 1
        for i in range(1, n):
            result.append(result[index-1]*nums[i-1])
            index += 1
        right = 1
        for i in range(n-1, -1, -1):
            if(i < n-1):
                right *= nums[i+1]
            result[i] *= right
                
        return(result)
                
        return(result)
            
        
# @lc code=end

