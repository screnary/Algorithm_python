""" 
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # check if this binary tree is ballanced
        if root is None:
            return True  # boundary condition, think about the leaf
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if root is None: return 0
        d_l = self.depth(root.left)
        d_r = self.depth(root.right)
        return 1 + max(d_l, d_r)
