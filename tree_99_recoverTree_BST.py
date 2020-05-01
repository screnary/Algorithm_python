""" 二叉搜索树中的两个节点被错误地交换。
请在不改变其结构的情况下，恢复这棵树。
直接方法：
1，inorder traverse，得到基本有序的list
2，从list中找出两个交换的数x,y
3，再次遍历tree，重新交换x,y
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = self.inorder(root)
        x, y = self.find_two_swapped(arr)

        def recover(root, count):
            if root:
                if root.val == x or root.val == y:
                    root.val = y if root.val == x else x
                    count -= 1
                    if count == 0: return
                recover(root.left, count)
                recover(root.right, count)
        
        recover(root, 2)       
    
    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
 
    def find_two_swapped(self, arr):
        x, y = -1, -1
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                y = arr[i+1]
                if x == -1:
                    # find first swapped
                    x = arr[i]
                else: # find second swapped
                    break
        return x, y
    

    def recoverTree_new(self, root):
        """
        通过递归方式，在中序遍历过程中寻找 two swapped
        BST中序遍历的性质：得到的是ascending array
        time: O(N)
        space，递归调用堆栈大小: O(H), H为树高度
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def find_two_swapped(root: TreeNode):
            nonlocal x, y, pred
            if root is None:
                return
            
            find_two_swapped(root.left)
            if pred and root.val < pred.val:
                y = root
                # first swap occurence
                if x is None:
                    x = pred 
                # second swap occurence
                else:
                    return
            pred = root
            find_two_swapped(root.right)
        
        x = y = pred = None
        find_two_swapped(root)
        x.val, y.val = y.val, x.val
