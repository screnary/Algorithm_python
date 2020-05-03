""" 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None

        return self.genBST(nums, 0, n-1)
        
    def genBST(self, arr, l, r):
        # ref merge sort
        if l > r:
            return None
        if l == r:
            return TreeNode(arr[l])
        mid = l + (r-l)//2
        root = TreeNode(arr[mid])
        root.left = self.genBST(arr, l, mid-1)
        root.right = self.genBST(arr, mid+1, r)
        return root
