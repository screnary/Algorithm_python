""" 两数之和 IV - 输入 BST
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = self.inorder(root)
        n = len(arr)
        if n == 0: return False
        for i in range(n-1):
            if (k - arr[i]) in arr[i+1:]:
                return True
        return False 
    
    def findTarget_2pointers(self, root, k):
        arr = self.inorder(root)
        l = 0
        r = len(arr)-1
        while l < r:
            if arr[l] + arr[r] == k:
                return True
            if arr[l] + arr[r] < k:
                l += 1
            elif arr[l] + arr[r] > k:
                r -= 1
        return False
    
    def inorder(self, root):
        if root is None: return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
