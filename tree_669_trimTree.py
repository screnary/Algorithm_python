""" 修剪二叉搜索树
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        # check cur root:
        # find valid val <=R, and val >=L
        root = self.search_node(root, L, R)
        if root:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        return root
    
    def search_node(self, root, L, R):
        while root:
            if root.val > R:
                root = root.left
            elif root.val < L:
                root = root.right
            else:
                break
        return root
