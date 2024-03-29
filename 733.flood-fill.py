#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from typing import List


def fill(board: List[List[int]], x, y, colour) -> List[List[int]]:
    m = len(board)
    val = board[x][y]
    board[x][y] = colour
    n = len(board[0])
    if (x+1 <= m-1 and board[x+1][y] == val):
        fill(board, x+1, y, colour)
    if (x-1 >= 0 and board[x-1][y] == val):
        fill(board, x-1, y, colour)
    if (y+1 <= n-1 and board[x][y+1] == val):
        fill(board, x, y+1, colour)
    if (y-1 >= 0 and board[x][y-1] == val):
        fill(board, x, y-1, colour)

    return board


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return fill(image, sr, sc, color)

# @lc code=end
