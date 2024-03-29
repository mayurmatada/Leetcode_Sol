#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info = [(p, s) for p, s in zip(position, speed)]
        stack = []
        
        for pos,spe in sorted(info)[::-1]:
            stack.append((target-pos)/spe)
            if (len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop(-1) 
        
        return len(stack)
        
        
# @lc code=end

