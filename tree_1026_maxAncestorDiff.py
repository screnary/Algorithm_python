# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, up, low):
            if root is None:
                # if search out of this path, do nothing and return
                return
            # maxD is this max(node - upper, node - lower, pre_res)
            self.res = max(abs(root.val - up), abs(root.val - low), self.res)
            up = max(up, root.val)  # update path upper
            low = min(low, root.val)
            # traverse left and right
            dfs(root.left, up, low)
            dfs(root.right, up, low)

        dfs(root, root.val, root.val)
        return self.res
