# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        self.sum_helper(root)
        return self.res

    def sum_helper(self, node):
        if node is None:
            return
        if node.left is not None and node.left.left is None and node.left.right is None:
            # if node has left leaf
            self.res += node.left.val
        self.sum_helper(node.left)
        self.sum_helper(node.right)
