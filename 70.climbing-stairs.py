#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        if (n % 2 == 0):
            x = int(n/2)
            y = 0
            while (x >= 0):
                count += ((math.factorial(x+y)) /
                          (math.factorial(x)*math.factorial(y)))
                x -= 1
                y += 2
        elif (n % 2 == 1):
            x = int((n-1)/2)
            y = 1
            while (x >= 0):
                count += ((math.factorial(x+y)) /
                          (math.factorial(x)*math.factorial(y)))
                x -= 1
                y += 2
        return int(count)
# @lc code=end
