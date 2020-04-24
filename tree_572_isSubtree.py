# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None: return False  # search out of s
        cpr = self.isSame(s, t)  # search in whole tree
        cpr_l = self.isSubtree(s.left, t)  # search in left tree
        cpr_r = self.isSubtree(s.right, t)  # search in right tree
        return cpr or cpr_l or cpr_r

    def isSame(self, root1, root2):
        if (root1 is None) and (root2 is None): return True
        if (root1 is None) or (root2 is None): return False
        if (root1.val != root2.val): return False
        return self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)

    def isSubtree_str(self, s, t):
        ss = self.tree2str(s)
        ts = self.tree2str(t)
        return ts in ss

    def tree2str(self, root):
        if root is None:
            return '#'
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        tree_pre = '*' + str(root.val) + left + right
        return tree_pre
