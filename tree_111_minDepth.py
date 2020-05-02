"""最小深度是从根节点到最近叶子节点的最短路径上的节点数量。"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
MAX_INT = sys.maxsize

class Solution:
    def minDepth_dfs(self, root: TreeNode) -> int:
        # 快
        if root is None:
            return 0
        self.minD = MAX_INT

        def dfs(node, d):
            if node.left is None and node.right is None:
                if self.minD > d:
                    self.minD = d
                return
            if node.left:
                dfs(node.left, d+1)
            if node.right:
                dfs(node.right, d+1)

        dfs(root, 1)
        return self.minD
    
    def minDepth_dc1(self, root):
        # 快
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        # case discussion:
        if root.left:
            md_l = self.minDepth(root.left)
        else:
            md_l = MAX_INT
        if root.right:
            md_r = self.minDepth(root.right)
        else:
            md_r = MAX_INT
        return 1 + min(md_l, md_r)
    
    def minDepth_dc2(self, root):
        # 速度慢
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        # case discussion:
        if not root.left:
            # if left is None, search right
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        # if has both left and right children
        md_l = self.minDepth(root.left)
        md_r = self.minDepth(root.right)
        return 1 + min(md_l, md_r)
    
    def minDepth_layer(self, root):
        # 层序遍历，速度还行， 内存少
        depth = 0
        if root is None:
            return 0
        stack = [root]
        while stack:
            n = len(stack)
            depth += 1
            for _ in range(n):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                if not node.left and not node.right:
                    return depth
