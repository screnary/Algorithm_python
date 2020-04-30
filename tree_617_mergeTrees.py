# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees_bk(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        root = self.__node_merge(t1, t2)
        if t1 is None or t2 is None:
            return root
        root.left = self.mergeTrees_bk(t1.left, t2.left)
        root.right = self.mergeTrees_bk(t1.right, t2.right)
        return root        
    
    def __node_merge(self, root1, root2):
        if root1 is None and root2 is None:
            return None
        elif root1 is not None and root2 is None:  # elif is not neccesary, use if
            return root1
        elif root1 is None and root2 is not None:
            return root2
        else:
            return TreeNode(root1.val + root2.val)
    
    def mergeTrees(self, t1, t2):
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
