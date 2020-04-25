"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # if cur level is larger than capacity of levels
            # this operation is pre-order
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            # traverse this level
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)

        helper(root, 0)
        return levels
