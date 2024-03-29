
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def maxdepth(self, node: TreeNode) -> int:
        if node is None:
            return 0
        else:
            ldepth = self.maxdepth(node.left)
            rdepth = self.maxdepth(node.right)
        self.diameter = max(self.diameter, ldepth+rdepth)
        return max(ldepth+1, rdepth+1)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdepth(root)
        return self.diameter
