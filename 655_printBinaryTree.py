"""
print Binary Tree:
1, get the result chart size (H, 2^H -1)
2, dfs (preorder) fill the chart
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        h = self.getHeight(root)
        w = (1<<h) - 1  # 2^h -1
        res = [["" for _ in range(w)] for _ in range(h)]
        self.fill_chart(res, root, 0, 0, w)
        return res
    
    def fill_chart(self, res, root, depth, l, r):
        """ DFS
            res: the chart to fill,
            root: cur node
            depth: cur depth
            l,r: for this node, left/right boundary in chart row
        """
        if root is None: return  # do nothing
        # fill root
        res[depth][(l+r)//2] = str(root.val)
        self.fill_chart(res, root.left, depth+1, l, (l+r)//2)
        self.fill_chart(res, root.right, depth+1, (l+r)//2 + 1, r)

    def getHeight(self, root):
        if root is None: return 0
        h_l = self.getHeight(root.left)
        h_r = self.getHeight(root.right)
        return 1 + max(h_l, h_r)
