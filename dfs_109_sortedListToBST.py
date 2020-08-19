"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """ input| head: ListNode
           output| TreeNode
        """
        # 1. get the median of the list, interval [left, right)
        def getMedian(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        # 2. build BST using the median of sorted list
        def buildBST(left, right):
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(val=mid.val)
            root.left = buildBST(left, mid)
            root.right = buildBST(mid.next, right)
            return root
        
        return buildBST(head, None)
        