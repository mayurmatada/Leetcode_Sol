#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        cpy = s
        for i in range(0, len(s)):
            cpy = s
            cpy = cpy.replace(s[:i], "")
            if(cpy == ""):
                return True
        return False
        
# @lc code=end

