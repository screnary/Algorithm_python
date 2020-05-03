""" 根据一棵树的前序遍历与中序遍历构造二叉树。
你可以假设树中没有重复的元素.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return None
        self.prelist = preorder
        self.dict = {}
        for i,n in enumerate(inorder):
            self.dict[n] = i
        def build_from_pre_in(pre_id, in_l, in_r):
            # pre_id is the start root idx from prelist
            # l,r is the left,right boundary of this list (include)
            if in_l > in_r:
                return None
            cur_val = self.prelist[pre_id]
            pivot = self.dict[cur_val]
            root = TreeNode(cur_val)
            root.left = build_from_pre_in(pre_id+1, in_l, pivot-1)
            root.right = build_from_pre_in(pre_id + pivot-in_l + 1, pivot+1, in_r)
            return root
        return build_from_pre_in(0, 0, len(inorder)-1)
