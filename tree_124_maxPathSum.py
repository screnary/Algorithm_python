""" 给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# import sys
# MAX_INT = sys.maxsize

class Solution:
    def maxPathSum_good(self, root):
        def max_gain(node):
            # post order traverse
            nonlocal max_sum
            if node is None:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # max path with node as the top most node
            merge_gain = left_gain + right_gain + node.val
            if merge_gain > max_sum:
                max_sum = merge_gain
            
            return node.val + max(left_gain, right_gain)
        
        max_sum = float('-inf')
        max_gain(root)
        return max_sum

    # def __init__(self):
    #     self.maxPath = -MAX_INT

    # def maxPathSum(self, root: TreeNode) -> int:
    #     # too slow
    #     if root is None: return  # do nothing
    #     tmp = self.getMaxPathPerNode(root)
    #     if tmp > self.maxPath:
    #         self.maxPath = tmp  # update state
    #     self.maxPathSum(root.left)
    #     self.maxPathSum(root.right)
    #     return self.maxPath

    # def getMaxPathPerNode(self, root):
    #     if root is None:
    #         return 0
    #     mp_l = self.dfs(root.left, 0, -MAX_INT)
    #     mp_r = self.dfs(root.right, 0, -MAX_INT)
    #     # print(mp_l, mp_r)
    #     return max(mp_l+root.val, mp_r+root.val, mp_l+mp_r+root.val, root.val)

    # def dfs(self, root, tmp, max_p):
    #     if root is None:
    #         return max_p
    #     if tmp + root.val > max_p:
    #         max_p = tmp+root.val
    #     max_l = self.dfs(root.left, tmp + root.val, max_p)
    #     max_r = self.dfs(root.right, tmp + root.val, max_p)
    #     return max(max_l, max_r)
