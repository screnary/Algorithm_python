# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val: return False

        # 若该节点值相同，继续遍历比较其他节点
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
