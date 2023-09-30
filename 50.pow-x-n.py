#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def powering(self, x:float, n: int,  ori):
        if(n%2 == 0):
            return self.powering(x*x, n/2, ori)
        elif(n == 1):
            return x
        else:
            return self.powering((x*x*ori), (n-1)/2, ori)
    def myPow(self, x: float, n: int) -> float:
        pow = 1
        x = 1/x if n < 0 else x
        if(n==0):
            return 1
        n = -n if n < 0 else n
        return self.powering(x, n, x)
# @lc code=end

