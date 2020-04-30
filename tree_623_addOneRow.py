"""
输入的深度值 d 的范围是：[1，二叉树最大深度 + 1]。
输入的二叉树至少有一个节点。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            tmp = TreeNode(v)
            tmp.left = root
            return tmp

        queue = []
        queue.append((root, 1))  # (node, depth)
        while queue:
            node, depth = queue.pop(0)  # FIFO
            if depth == d-1:  # is the target layer's parent
                lo, ro = node.left, node.right  # original children
                # left update
                tmp = TreeNode(v)
                tmp.left = lo
                node.left = tmp
                # right update
                tmp = TreeNode(v)
                tmp.right = ro
                node.right = tmp
                continue

            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        
        return root
