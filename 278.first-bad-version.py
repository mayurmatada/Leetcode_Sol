#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while (True):
            if (isBadVersion(int((l+r)/2)) == True):
                if (isBadVersion(int((l+r)/2)-1) == False):
                    return int((l+r)/2)
                else:
                    r = int((l+r)/2)
            if (isBadVersion(int((l+r)/2)) == False):
                if (isBadVersion(int((l+r)/2)+1) == True):
                    return int((l+r)/2)+1
                else:
                    l = int((l+r)/2)
# @lc code=end
