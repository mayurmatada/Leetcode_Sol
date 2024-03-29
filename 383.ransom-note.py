#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga_list = list(magazine)
        for k in ransomNote:
            if (k in maga_list):
                maga_list.remove(k)
            else:
                return False
        return True
# @lc code=end
