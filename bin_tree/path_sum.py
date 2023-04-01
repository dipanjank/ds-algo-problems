"""
Return True if a binary tree has a path with a sum S."
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def has_path_sum(self, root: Optional[TreeNode], target: int) -> bool:
        if root is None:
            return False

        return self.has_sum(root, 0, target)

    def is_leaf(self, root):
        return root.left is None and root.right is None

    def has_sum(self, root, sum_path, target):
        if not root:
            return False

        sum_path += root.val

        if self.is_leaf(root) and sum_path == target:
            return True
        else:
            return self.has_sum(root.left, sum_path, target) \
                or self.has_sum(root.right, sum_path, target)