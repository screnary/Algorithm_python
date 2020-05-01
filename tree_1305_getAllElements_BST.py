"""给你 root1 和 root2 这两棵二叉搜索树。
请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。 
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def inorder(root, v):
            if root is None:
                return
            inorder(root.left, v)
            v.append(root.val)
            inorder(root.right, v)

        def merge(arr1, arr2):
            res = []
            i,j = 0,0
            len1, len2 = len(arr1), len(arr2)
            while i < len1 or j < len2:
                if j == len2:
                    res.append(arr1[i])
                    i += 1
                elif i == len1:
                    res.append(arr2[j])
                    j += 1
                elif arr1[i] <= arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            return res

        nums1, nums2 = [], []
        inorder(root1, nums1)
        inorder(root2, nums2)
        return merge(nums1, nums2)
