"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

来源：力扣（LeetCode） 链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if key == root.val:
            # found, delete it
            if root.left is None and root.right is None:
                return None  # case 1
            elif root.left is None:
                return root.right  # case 2
            elif root.right is None:
                return root.left
            elif root.left is not None and root.right is not None:
                # case 3
                min_val = self.get_min_re(root.right)
                root.val = min_val
                root.right = self.deleteNode(root.right, min_val)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        return root

    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root.val
    
    def get_min_re(self, root):
        if root.left is None:
            return root.val
        min_val = self.get_min_re(root.left)
        return min_val  # must write this as output
