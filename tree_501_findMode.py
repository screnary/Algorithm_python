""" 
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：
结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树

来源：力扣（LeetCode） 链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        # inorder traverse
        arr = self.inOrder(root)
        arr.append('#')
        # sliding window
        i = 0
        tmp_count = 1
        counts = [(0,0)]
        while i < len(arr)-1:
            if arr[i] == arr[i+1]:
                tmp_count += 1
                i += 1
            else:
                if counts[0][1] < tmp_count:
                    # init counts
                    counts = [(arr[i], tmp_count)]
                elif counts[0][1] == tmp_count:
                    # append to counts
                    counts.append((arr[i], tmp_count))
                tmp_count = 1  # reset tmp count
                i += 1
        return [item[0] for item in counts]                
    
    def inOrder(self, root):
        if root is None:
            return []
        left = self.inOrder(root.left)
        right = self.inOrder(root.right)
        cur = root.val
        return left + [cur] + right
