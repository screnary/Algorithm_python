""" 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        def dfs(root, numstr):
            if root is None: return
            if root.left is None and root.right is None:
                res.append(numstr+str(root.val))
                return
            dfs(root.left, numstr+str(root.val))
            dfs(root.right, numstr+str(root.val))
        dfs(root, "")
        return sum(list(map(int, res)))

    def sumNumbers_better(self, root):
        def helper(root, pre):
            if not root: return 0
            pre = pre*10 + root.val
            if not root.left and not root.right:
                return pre
            return helper(root.left, pre) + helper(root.right, pre)
        return helper(root, 0)