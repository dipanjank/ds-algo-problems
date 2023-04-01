"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to
right, then right to left for the next level and alternate between).
"""
from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        items_by_level = defaultdict(list)
        self.traverse(root, 1, items_by_level)
        end = max(items_by_level.keys())
        result = []
        for i in range(1, end+1):
            if i % 2 == 1:
                result.append(items_by_level[i])
            else:
                v = list(reversed(items_by_level[i]))
                result.append(v)
        return result

    def traverse(self, node, level, items):
        items[level].append(node.val)
        if node.left:
            self.traverse(node.left, level+1, items)
        if node.right:
            self.traverse(node.right, level + 1, items)


if __name__ == "__main__":
    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    s = Solution()
    print(s.zigzagLevelOrder(root))

