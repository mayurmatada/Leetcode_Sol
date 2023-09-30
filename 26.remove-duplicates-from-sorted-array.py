#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(nums == []):
            return 0
        i = 0
        while(i < len(nums)):
            if(i != len(nums)-1 and len(nums) != 1):  
                try:       
                    while(len(nums) != 1 and nums[i] == nums[i+1] ):
                        nums.pop(i+1)
                except:
                    pass
            i += 1
        return len(nums)
            
        
# @lc code=end

