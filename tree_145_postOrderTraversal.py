# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
    def postorderTraversal_iteration_method(self, root):
        if root is None: return []
        res = deque([])
        stack = [root]
        while stack:
            node = stack.pop()
            res.appendleft(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return list(res)
