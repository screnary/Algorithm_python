""" 
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # get all the subtrees, save to a dict/list
        self.dict = {}  # {treestr_serialize: count}
        self.sbroots = []
        # self.getSubtrees(root)  # when count achieves 2, record to sbroots
        self.tree2str(root)
        # print(list(self.dict.items()))

        # return the roots of the duplicated subtrees
        return self.sbroots

    def tree2str(self, root):
        if root is None:
            return '#'
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        str_po = str(root.val) + ',' + left + ',' + right  # pre-order string, serialize
        # (post order) operation on str preorder,
        if str_po in self.dict:
            self.dict[str_po] += 1
        else:
            self.dict[str_po] = 1
        if self.dict[str_po] == 2:
            self.sbroots.append(root)
        return str_po
