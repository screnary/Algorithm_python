""" 根据一棵树的中序遍历与后序遍历构造二叉树。
你可以假设树中没有重复的元素.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        l_num = len(postorder)
        if l_num == 0: return None
        self.postlist = postorder
        self.dict = {}
        for i,n in enumerate(inorder):
            self.dict[n] = i
        def build_from_post_in(post_id, in_l, in_r):
            # pre_id is the start root idx from prelist
            # l,r is the left,right boundary of this list (include)
            if in_l > in_r:
                return None
            cur_val = self.postlist[post_id]
            pivot = self.dict[cur_val]
            root = TreeNode(cur_val)
            root.right = build_from_post_in(post_id-1, pivot+1, in_r)
            root.left = build_from_post_in(post_id - (in_r-pivot) - 1, in_l, pivot-1)
            return root
        return build_from_post_in(l_num-1, 0, l_num-1)
