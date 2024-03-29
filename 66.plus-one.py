#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if (digits[i] == 9 and i != 0):
                digits[i] = 0
            elif (i != 0):
                digits[i] += 1
                return digits
            elif (i == 0 and digits[i] != 9):
                digits[i] += 1
                return digits
            else:
                digits.insert(0, 1)
                for k in range(len(digits)-1, 0, -1):
                    digits[k] = 0
                return digits


# @lc code=end
