#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        midflag = False
        s_l = list(s)
        for k in s_l:
            if (k != '0'):
                s_l[s_l.index(k)] = '0'
                if (k in s_l):
                    s_l[s_l.index(k)] = '0'
                    count += 1
                else:
                    midflag = True
        if (midflag == True):
            return (count*2)+1
        else:
            return count*2
# @lc code=end
