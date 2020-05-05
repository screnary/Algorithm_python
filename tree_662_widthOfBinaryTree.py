""" 二叉树最大宽度
给定一个二叉树，编写一个函数来获取这个树的最大宽度。
树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。
每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root):
        # O(n), record position index: pos
        if root is None: return 0
        max_w, pos = 0, 1
        queue = [(root, pos)]
        while queue:
            n = len(queue)
            new_layer = True
            for _ in range(n):
                # last node of this layer, is the right pos
                node, pos = queue.pop(0)
                if node.left:
                    queue.append((node.left, pos*2))
                if node.right:
                    queue.append((node.right, pos*2 + 1))
                if new_layer:
                    # first node of this layer, is the left pos
                    left = pos
                    new_layer = False
            cur_w = pos - left + 1
            max_w = cur_w if cur_w > max_w else max_w
        return max_w

    def widthOfBinaryTree_too_slow(self, root: TreeNode) -> int:
        # out of time limit, O(n^2)
        if root is None:
            return 0
        max_w = 0
        queue = [root]  # FIFO
        while queue:
            n = len(queue)
            if max_w < n:
                max_w = n
            for _ in range(n):
                node = queue.pop(0)
                # enque, even if child is None
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    queue.append(None)
                    queue.append(None)
            # strip the head and tail None nodes
            l, r = 0, len(queue)-1
            while l <= r:
                if queue[l] is None:
                    l += 1
                elif queue[r] is None:
                    r -= 1
                else:
                    break
            if l > r:
                queue = []
            else:
                queue = queue[l:r+1]
        return max_w
