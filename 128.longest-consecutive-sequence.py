#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = {}
        nums.sort()
        if(nums == []):
            return 0
        
        for i in nums:
            if i-1 in counter:
                counter[i] = counter.pop(i-1)
                counter[i] += 1
            elif (i in counter):
                pass
            else:
                counter[i] = 1
        
        val = list(counter.values())
        val.sort()
        return val[len(val)-1]
# @lc code=end

