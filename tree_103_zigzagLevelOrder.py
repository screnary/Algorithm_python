""" 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None: return []
        queue = [root]
        reverse = False
        while queue:
            n = len(queue)
            cur_layer = []
            for _ in range(n):
                node = queue.pop(0)  # FIFO
                # insert to cur_layer
                cur_layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse:
                res.append(cur_layer[::-1])
            else:
                res.append(cur_layer)
            reverse = not reverse
        return res
    
    def zigzagLevelOrder_DFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque

        if root is None:
            return []

        results = []
        def dfs(node, level):
            if level >= len(results):  # if cur level is larger than capacity of levels
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:  # process order in this section
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:  # this order need to be preserved
                if next_node is not None:
                    dfs(next_node, level+1)

        # normal level order traversal with DFS
        dfs(root, 0)

        return [list(queue) for queue in results]
