""" 给定一个二叉树，原地将它展开为链表。 """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return
        self.flatten(root.right)
        self.flatten(root.left)
        # operation here: post order
        root.right = self.pre
        root.left = None
        self.pre = root