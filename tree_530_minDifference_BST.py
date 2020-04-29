""" 
直接递归求解；
还可以 中序遍历+sliding window。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # terminate condition
        if root is None:
            return 2<<32  # return the largest
        # current node operation, the root node at least has one child
        a = self.get_max(root.left)
        b = self.get_min(root.right)
        left_d = self.getMinimumDifference(root.left)
        right_d = self.getMinimumDifference(root.right)
        cur_d = min(abs(root.val - a), abs(root.val - b))
        return min(cur_d, left_d, right_d)

    def get_min(self, root):
        if root is None: return -2<<32  # if minused, enlarge
        while root.left is not None:
            root = root.left
        return root.val

    def get_max(self, root):
        if root is None: return -2<<32  # if minused, enlarge
        while root.right is not None:
            root = root.right
        return root.val

    def is_leaf(self, root):
        return root.left is None and root.right is None
