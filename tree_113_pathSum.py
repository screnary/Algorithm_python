"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.paths = []
        if root is None: return []
        def dfs(node, target, path):
            if not node:
                return path
            target -= node.val
            path.append(node.val)
            if not node.left and not node.right:
                if target==0:
                    self.paths.append(path)
                return path[:-1]
            path = dfs(node.left, target, path)
            path = dfs(node.right, target, path)
            return path[:-1]

        dfs(root, sum, [])
        return self.paths

    def pathSum_refine(self, root, sum):
        self.res = []
        
        def dfs(root,tmp,sum):
            if not root: return 
            
            if not root.left and not root.right and root.val == sum:
                self.res.append(tmp+[root.val])
            
            dfs(root.left,tmp+[root.val], sum - root.val)  # do not change tmp, sum states while deeper searching
            dfs(root.right,tmp+[root.val], sum - root.val)

        dfs(root, [], sum)
        return self.res