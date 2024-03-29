#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        cur = 0
        back = n
        while(cur <= back):
            while((ord(s[cur]) <= 30 or ord(s[cur]) >= 39) and (ord(s[cur]) <= 65 or ord(s[cur]) >= 90) and (ord(s[cur]) <= 97 or ord(s[cur]) >= 122)):
                cur += 1;
            while((ord(s[cur]) <= 30 or ord(s[cur]) >= 39) and (ord(s[cur]) <= 65 or ord(s[cur]) >= 90) and (ord(s[cur]) <= 97 or ord(s[cur]) >= 122)):
                back -= 1;
            if(s[cur] != s[back]):
                return False
        return True
            
        
# @lc code=end

