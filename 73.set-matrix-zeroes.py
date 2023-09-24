#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = [[], []]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if(matrix[i][j] == 0):
                    zeroes[0].append(i)
                    zeroes[1].append(j)
        for k in zeroes[0]:
                matrix[k][:] = [0 for i in range(0, len(matrix[0])) ]
        for l in zeroes[1]:
                for m in range(0, len(matrix)):
                    matrix[m][l] = 0                

        
# @lc code=end

