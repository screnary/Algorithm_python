""" 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组. """

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None: return []
        res = []
        queue = [root]
        while queue:
            n = len(queue)
            tmp_sum = 0
            for _ in range(n):
                node = queue.pop(0)
                tmp_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp_sum / n)
        return res
