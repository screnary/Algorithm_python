# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.total = 0

    def findTilt(self, root: TreeNode) -> int:
        if root is None: return 0
        self.treesum(root)
        return self.total
    
    def treesum(self, root):
        if root is None: return 0
        sl = self.treesum(root.left)
        sr = self.treesum(root.right)
        # compute tilt of this node
        self.total += abs(sl-sr)
        return root.val + sl + sr
