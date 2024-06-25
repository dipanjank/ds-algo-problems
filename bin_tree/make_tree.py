"""
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(inorder, preorder):
    if not inorder and not preorder:
        return None
    if len(inorder) == 1 and len(preorder) == 1:
        assert inorder[0] == preorder[0]
        return TreeNode(val=inorder[0])
    else:
        root_val = preorder[0]
        ri_in = inorder.index(root_val)
        in_left = inorder[0: ri_in]
        in_right = inorder[ri_in + 1:]

        pre_idx = preorder.index(in_left[-1])
        pre_left = preorder[1: pre_idx+1]
        pre_right = preorder[pre_idx+1:]

        return TreeNode(
            val=root_val,
            left=make_tree(in_left, pre_left),
            right=make_tree(in_right, pre_right),
        )


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = make_tree(inorder, preorder)

    def print_tree(node):
        print(f"Node: {node.val}, left: {node.left.val if node.left else None}, right: {node.right.val if node.right else None}")
        if node.left:
            print_tree(node.left)
        if node.right:
            print_tree(node.right)
    print_tree(root)
