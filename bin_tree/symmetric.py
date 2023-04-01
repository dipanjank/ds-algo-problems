from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def is_symmetric(self, root):
        if not root:
            return True

        q = deque()

        nodes_by_level = defaultdict(list)

        q.appendleft((1, root))
        while q:
            level, node = q.pop()
            nodes_by_level[level].append(node.val if node else None)
            if not node:
                continue

            if node.left:
                q.appendleft((level+1, node.left))
            else:
                q.appendleft((level+1, None))
            if node.right:
                q.appendleft((level+1, node.right))
            else:
                q.appendleft((level + 1, None))

        max_level = max(nodes_by_level.keys())

        for i in range(1, max_level+1):
            vals = nodes_by_level[i]
            n = len(vals)
            mid = n // 2
            for i in range(mid):
                cmp = vals[n-i-1]
                if cmp is None and vals[i] is None:
                    continue
                if cmp == vals[i]:
                    continue
                else:
                    return False

        return True


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
        right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)),
    )
    sym = s.is_symmetric(root)
    assert sym





