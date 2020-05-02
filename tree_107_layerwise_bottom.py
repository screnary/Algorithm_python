# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root, depth):
            if not root: return 
            if depth == len(res):
                res.insert(0, [])
            res[-(depth+1)].append(root.val)
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        helper(root, 0)
        return res

    def levelOrderBottom_iteration(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root: return []
        queue = deque()
        queue.appendleft(root)
        res = []
        while queue:  # if this layer has node
            tmp = []
            n = len(queue)
            for _ in range(n):
                # get cur layer's node.val
                node = queue.pop()
                tmp.append(node.val)
                # enqueue the next layer nodes
                if node.left:
                    queue.appendleft(node.left)  # FIFO
                if node.right:
                    queue.appendleft(node.right)
            res.insert(0, tmp)
        return res
