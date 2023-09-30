#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}" : "{", "]" : "[", ")" : "("}
        cur = []
        for i in s:
            if(i == "(" or i == "[" or i== "{"):
                cur.append(i)
            else:
                if(len(cur) == 0):
                    return False
                else:
                    if(cur[-1] == brackets[i]):
                        cur.pop(-1)
                    else:
                        return False
        if len(cur) == 0: 
            return True
        else: 
            return False

        
            
            
        
# @lc code=end

