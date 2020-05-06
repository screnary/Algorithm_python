

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.res = float('inf')
        def dfs(root, low):
            if not root or root.val >= self.res:
                return  # stop traversing this route

            if root and root.val > low and root.val < self.res:
                self.res = root.val
                return  # update status and return to upper loop
            
            # searching the possible routes
            dfs(root.left, low)
            dfs(root.right, low)

        dfs(root, root.val)
        if self.res == float('inf'):
            return -1
        return self.res
