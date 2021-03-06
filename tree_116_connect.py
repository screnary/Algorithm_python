"""
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect_bfs(self, root):
        if root is None: return None
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i < n-1 and queue:  # the last node in this layer, do not connect
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    def connect(self, root):
        """ divide conquer, O(1) space """
        if not root or (not root.left and not root.right):
            return root
        if root.left and root.right:
            root.left.next = root.right
            root.right.next = self.getNextChild(root)
        if not root.left:
            root.right.next = self.getNextChild(root)
        if not root.right:
            root.left.next = self.getNextChild(root)

        root.right = self.connect(root.right)
        root.left = self.connect(root.left)
        return root
    
    def getNextChild(self, root):
        # search same level neighbor, from parent level nodes
        while root.next:
            if root.next.left:
                return root.next.left
            if root.next.right:
                return root.next.right
            root = root.next
        return None
