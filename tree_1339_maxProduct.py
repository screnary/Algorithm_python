""" 分裂二叉树的最大乘积 
给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。
由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。

每棵树最多有 50000 个节点，且至少有 2 个节点。
每个节点的值在 [1, 10000] 之间。

[注意：]
后序遍历，dfs2 在删边同时求树和，相较之前的前序的求和操作，重复计算大幅减少。
（上层节点求和，使用下层递归返回结果）
若在前序调用外部 sum_tree(node)，则每次都重复自底向上计算一遍。。。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        self.res = 0
        sum_total = self.sum_tree(root)
        def dfs2(root):
            if root is None: return 0
            cur = dfs2(root.left) + dfs2(root.right) + root.val
            # post order, compute from this node
            tmp_prod = cur * (sum_total - cur)
            self.res = tmp_prod if self.res < tmp_prod else self.res
            if cur > sum_total/2:
                return cur  # cut the tree
            return cur

        dfs2(root)
        return self.res % (10**9 + 7)

    def sum_tree(self, root):
        if root is None: return 0
        sum_l = self.sum_tree(root.left)
        sum_r = self.sum_tree(root.right)
        return root.val + sum_l + sum_r