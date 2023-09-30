#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
        

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {"A":[]}
        for word in strs:
            sortedword = "".join(sorted(word))
            try:
                result[sortedword].append(word)
            except:
                result[sortedword] = [word]
        del result["A"]
        return list(result.values())


# @lc code=end

