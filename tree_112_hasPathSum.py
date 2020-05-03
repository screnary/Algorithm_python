"""给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum_dfs(self, root: TreeNode, sum: int) -> bool:
        # only have to consider start from root
        self.flag = False
        if root is None: return False
        def dfs(node, target):
            if not node:
                return
            target -= node.val
            if not node.left and not node.right:
                if target==0:
                    self.flag = True
                return
            dfs(node.left, target)
            dfs(node.right, target)

        dfs(root, sum)
        return self.flag
    
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        sum -= root.val
        if not root.left and not root.right:  # reach leaf
            if sum == 0:
                return True
        in_l = self.hasPathSum(root.left, sum)
        in_r = self.hasPathSum(root.right, sum)
        return in_l or in_r
