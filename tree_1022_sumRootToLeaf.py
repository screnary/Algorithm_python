""" 
1022,从根到叶的二进制数之和
深度搜索遍历，获取binary num列表
binary2decimal
sum
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.sum = 0
        cursum = 0

        def dfs(root, cursum):
            if root is None:
                return
            cursum = (cursum << 1) + root.val
            if self.isleaf(root):
                self.sum += cursum
            else:
                dfs(root.left, cursum)
                dfs(root.right, cursum)

        dfs(root, cursum)

        return self.sum % (10**9 + 7)
    
    def sumRootToLeaf_(self, root: TreeNode) -> int:
        self.binnums = []
        self.binstr = ""
        def dfs(root):
            if root is None:
                return
            self.binstr = self.binstr + str(root.val)
            if self.isleaf(root):
                self.binnums.append(self.binstr)
                self.binstr = self.binstr[:-1]
            else:
                dfs(root.left)
                dfs(root.right)
                self.binstr = self.binstr[:-1]
        dfs(root)
        # print(self.binnums)
        decimal = [self.bin2decimal(num) for num in self.binnums]
        return sum(decimal) % (10**9 + 7)

    def isleaf(self, root):
        return root.left is None and root.right is None
    
    def bin2decimal(self, num):
        # 优化：binary 2 decimal 的运算，可以在dfs中简单实现，不需要维护binstr列表
        res = 0
        for (i,n) in enumerate(num[::-1]):
            res += int(n) << i
        return res
