from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def to_bst(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build_tree(nums)

    def build_tree(self, nums):
        if not nums:
            return None

        n = len(nums)
        mid = n // 2
        root = TreeNode(nums[mid])
        root.left = self.build_tree(nums[:mid])
        root.right = self.build_tree(nums[mid + 1:])
        return root