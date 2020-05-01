"""给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
暴力方法：
对节点进行全排序，按照输入顺序构成arr，由此生成BST；将BST前序编码，滤除重复树；
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from itertools import permutations
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        res = []
        memo = []
        nums = [n for n in range(1, n+1)]
        for arr in permutations(nums, len(nums)):
            root, strid = self.genBST(list(arr))
            if strid not in memo:
                memo.append(strid)
                res.append(root)
        return res

    def genBST(self, arr):
        root = TreeNode(arr.pop(0))
        while arr:
            root = self.add2BST(root, arr.pop(0))
        strid = self.tree2str(root)
        return root, strid
        
    def add2BST(self, node, num):
        if node is None:
            return TreeNode(num)
        if num < node.val:
            node.left = self.add2BST(node.left, num)
        if node.val < num:
            node.right = self.add2BST(node.right, num)
        return node

    def tree2str(self, root):
        if root is None:
            return ""
        return str(root.val) + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"
    
    # donot use itertools
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def back(nums_all,temp):
            if len(nums_all) == 0:
                res.append(temp)
                return
            for i in range(len(nums_all)):
                back(nums_all[:i]+nums_all[i+1:],temp+[nums_all[i]])
                
        t = []
        back(nums,t)
        return res
    

    def generateTrees_divide_conquer(self, n):
        """
        优雅解法，time and space = O(n*G(n)), O(4^n / n^{1/2}), G(n) 卡兰特数
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)
                
                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)
                
                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generate_trees(1, n) if n else []
