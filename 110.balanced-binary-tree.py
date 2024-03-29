#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depth(node: TreeNode) -> int:
    left_count = 0
    while (node.left != None):
        left_count += 1
        node = node.left
    return left_count


def diff(node):
    return (depth(node.left) - depth(node.right))


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (diff(node=root) > 1):
            return False
        return True

# @lc code=end
