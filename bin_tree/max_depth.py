from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.calc_max_depth(root)

    def calc_max_depth(self, root, max_depth=1):
        if root.left is None and root.right is None:
            return max_depth
        elif root.left is None:
            return self.calc_max_depth(root.right, max_depth + 1)
        elif root.right is None:
            return self.calc_max_depth(root.left, max_depth + 1)
        else:
            return max(
                self.calc_max_depth(root.left, max_depth + 1),
                self.calc_max_depth(root.right, max_depth + 1)
            )
