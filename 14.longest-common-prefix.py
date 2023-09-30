#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = ""
        for j in range(0, len(strs[0])):
            for k in range(1, len(strs)):
                try:
                    if(strs[k][j] != strs[0][j]):
                        return str(cur)
                except:
                    return str(cur)
            cur += strs[0][j]
        return str(strs)
        
# @lc code=end

