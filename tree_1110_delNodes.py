""" 删点成林
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        self.todel = to_delete
        if not to_delete: return self.res

        def del_dfs(root):
            if root is None: return None

            root.left = del_dfs(root.left)
            root.right = del_dfs(root.right)

            if root.val in self.todel:
                if root.left:
                    self.res.append(root.left)
                if root.right:
                    self.res.append(root.right)
                self.todel.remove(root.val)
                return None

            return root
        
        root = del_dfs(root)
        if root is not None:
            self.res.append(root)
        return self.res
