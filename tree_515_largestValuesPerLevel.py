# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        # init max_list
        max_list = []
        max_list.append(root.val)
        # broad first search
        queue = []
        queue.append((root, 0))
        while len(queue) > 0:
            item = queue.pop(0)
            node, level = item[0], item[1]
            if level == len(max_list):
                max_list.append(node.val)
            else:
                if max_list[level] < node.val:
                    max_list[level] = node.val

            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))
        
        return max_list
