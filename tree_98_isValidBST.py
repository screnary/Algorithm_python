""" 
inorder traverse, if not ascending, return False
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.isvalid = True
        self.inorder(root)
        return self.isvalid
    
    def inorder(self, root):
        if root is None:
            return []
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        cur = root.val
        if left and left[-1] >= cur:
            self.isvalid = False
        if right and right[0] <= cur:
            self.isvalid = False
        return left + [cur] + right
