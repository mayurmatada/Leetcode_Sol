#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = t
        for i in s:
               result = result.replace(i, "", 1)
        return result

        
# @lc code=end

