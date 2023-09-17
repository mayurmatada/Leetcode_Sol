#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        count = 0
        if(len(word1) < len(word2)):
            for i in word1:
                result = result + i
                result = result + word2[count]
                count = count + 1
            result = result + word2[count:]
        elif(len(word2) < len(word1)):
            for i in range(0, len(word2)):
                result = result + word1[i]
                result = result + word2[count]
                count = count  + 1
            result = result + word1[count:]
        else:
            for i in word1:
                result = result + i
                result = result + word2[count]
                count = count + 1
        return result

        
# @lc code=end

