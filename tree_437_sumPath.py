# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pathnum = 0
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return self.pathnum  # this has two functional: 1) sub recursive's termination, 2) Null tree exception
        self.__helper(root, 0, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.pathnum  # output after all the space has been searched

    def __helper(self, node, tmp_sum, sum):
        if not node: return
        # operation on this node
        tmp_sum += node.val
        if tmp_sum == sum:
            self.pathnum += 1
        self.__helper(node.left, tmp_sum, sum)
        self.__helper(node.right, tmp_sum, sum)
