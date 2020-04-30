"""
101, 对称二叉树
递归结束条件：
    都为空指针则返回 true
    只有一个为空则返回 false
递归过程：
    判断两个指针当前节点值是否相等
    判断 A 的右子树与 B 的左子树是否对称
    判断 A 的左子树与 B 的右子树是否对称
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None: return True
        if t1 is None or t2 is None: return False
        return (t1.val == t2.val) and \
            self.isMirror(t1.left, t2.right) and \
            self.isMirror(t1.right, t2.left)