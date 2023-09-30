#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        cur = 0
        result = 0
        while(cur < len(s)):
            if(s[cur] == "I"):
                if(cur != len(s)-1):
                    if(s[cur+1] == "V"):
                        result += 4
                        cur += 2
                    elif(s[cur+1] == "X"):
                        result += 9
                        cur += 2
                    else:
                        result += 1
                        cur += 1
                else:
                    result += 1
                    cur += 1
            elif(s[cur] == "X"):
                if(cur != len(s)-1):
                    if(s[cur+1] == "L"):
                        result += 40
                        cur += 2
                    elif(s[cur+1] == "C"):
                        result += 90
                        cur += 2
                    else:
                        result += 10
                        cur += 1
                else:
                    result += 10
                    cur += 1
            elif(s[cur] == "C"):
                if(cur != len(s)-1):
                    if(s[cur+1] == "D"):
                        result += 400
                        cur += 2
                    elif(s[cur+1] == "M"):
                        result += 900
                        cur += 2
                    else:
                        result += 100
                        cur += 1
                else:
                    result += 100
                    cur += 1
            elif(s[cur] == "V"):
                result += 5
                cur += 1
            elif(s[cur] == "L"):
                result += 50
                cur += 1
            elif(s[cur] == "D"):
                result += 500
                cur += 1
            elif(s[cur] == "M"):
                result += 1000
                cur += 1
        return result
# @lc code=end

