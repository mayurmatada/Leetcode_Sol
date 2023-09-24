#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        exponent = 0
        number1 = 0
        digits = []
        for i in num1:
            digits.append(ord(i)-48)
        digits = digits[::-1]
        for j in digits:
            number1 = number1 + (j*(10**exponent))
            exponent = exponent + 1
        exponent = 0
        number2 = 0
        digits = []
        for k in num2:
            digits.append(ord(k)-48)
        digits = digits[::-1]
        for l in digits:
            number2 = number2 + (l*(10**exponent))
            exponent = exponent + 1
        return str(number1 * number2)

# @lc code=end

