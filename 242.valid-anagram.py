#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        modified = t
        for i in s:
            modified = modified.replace(i, "", 1)
        if(modified == "" and len(s) == len(t)):
            return True
        else:
            return False
        
# @lc code=end

