""" 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None: return 0
        self.diam = 0
        self.depth(root)
        return self.diam

    def depth(self, root):
        if root is None:
            return 0
        d_l = self.depth(root.left)
        d_r = self.depth(root.right)
        self.diam = max(d_l + d_r, self.diam)
        return 1+max(d_l, d_r)
