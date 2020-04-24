""" tree: [3,9,20,null,null,15,7] """
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.leaf = False  # for null element, when constructing

class Tree():
    def __init__(self, root=None):
        self.root = root
    
    def add(self, item):
        """ breadth first """
        node = TreeNode(item)
        if item == None:
            node.leaf = True

        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.left == None and not cur.leaf:
                    cur.left = node
                    return
                elif cur.right == None and not cur.leaf:
                    cur.right = node
                    return
                else:
                    if not cur.leaf:
                        queue.append(cur.left)
                        queue.append(cur.right)
    
    def construct_from_bflist(self, l):
        for v in l:
            self.add(v)

    def breadth_travel(self):
        queue = []
        queue.append(self.root)
        print("[", end = " ")
        while queue:
            cur = queue.pop(0)
            if cur is None:
                print("]")
                return
            print(cur.val, end = " ")
            if cur.left is not None or cur.leaf:
                queue.append(cur.left)
            if cur.right is not None or cur.leaf:
                queue.append(cur.right)
    
    def preorder(self, node):
        # terminate operation
        if node is None:
            return

        print(node.val, end = " ")  # output before traveling
        self.preorder(node.left)
        self.preorder(node.right)
    
    def inorder(self, node):
        # terminate operation
        if node is None:
            return

        self.preorder(node.left)
        print(node.val, end = " ")  # output between traveling
        self.preorder(node.right)
    
    def postorder(self, node):
        # terminate operation
        if node is None:
            return

        self.preorder(node.left)
        self.preorder(node.right)
        print(node.val, end = " ")  # output after traveling


class Solution:
    # N.O. 110. balanced binary tree
    def isBalanced(self, root: TreeNode) -> bool:
        # check if this binary tree is ballanced
        return self.depth_bottom_up(root) != -1

    def depth_bottom_up(self, root):
        if not root: return 0
        left = self.depth_bottom_up(root.left)
        if left == -1: return -1
        right = self.depth_bottom_up(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1
    
    def depth_top_down(self, root):
        if not root: return 0
        return max(self.depth_top_down(root.left), self.depth_top_down(root.right)) + 1
    
    # N.O. 1008, preorder construct Binary Tree (Binary searching tree)
    def bstFromPreorder(self, preorder) -> TreeNode:
        """ preorder is List[int] """
        def preorder_construct(lower=float('-inf'), upper=float('inf')):
            nonlocal idx  # the index of preorder list
            if idx == n:  # if every element in the list has been visited
                return None
            
            val = preorder[idx]
            if val < lower or val > upper:  # if not subject to node val rule
                return None
            
            # construct the tree in preorder
            root = TreeNode(val)
            idx += 1
            root.left = preorder_construct(lower, val)
            root.right = preorder_construct(val, upper)
            return root

        n = len(preorder)
        idx = 0
        return preorder_construct()
            

if __name__ == '__main__':
    # tree_l = [3, 9, 20, None, None, 15, 7]
    # tree_l = [1,2,2,3,3,None,None,4,4]
    # BF_tree = Tree()
    # BF_tree.construct_from_bflist(tree_l)
    # print(tree_l)
    # BF_tree.breadth_travel()
    # BF_tree.preorder(BF_tree.root)

    tree_l = [8,5,1,7,10,12]
    sol = Solution()
    tree_root = sol.bstFromPreorder(tree_l)
    BF_tree = Tree()
    BF_tree.preorder(tree_root)
