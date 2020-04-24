# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """paras:
        input: preorder: List[int]; inorder: List[int]
        output: TreeNode
        """
        self.prelist = preorder
        self.indict = {}
        # hash map, inorder index
        for i in range(len(inorder)):
            self.indict[inorder[i]] = i
        
        root = self.__recursive(0, 0, len(inorder)-1)
        return root
    
    def __recursive(self, pre_root, in_left, in_right):
        # terminate
        if in_left > in_right:
            return None
        # construct cur tree node
        root = TreeNode(self.prelist[pre_root])
        # find the index of root from inlist
        pivot = self.indict[self.prelist[pre_root]]
        
        # recursively, construct cur root's left/right sub tree
        root.left = self.__recursive(pre_root+1, in_left, pivot-1)
        root.right = self.__recursive(pre_root+(pivot-in_left)+1, pivot+1, in_right)

        return root  # return root node, as upper loop's left/right child
