"""输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """ input| l1: ListNode, l2: ListNode
           output| ListNode """
        pre = ListNode(None)
        l_new = pre
        while l1 is not None or l2 is not None:
            if l1 is None:
                l_new.next = l2
                break
            elif l2 is None:
                l_new.next = l1
                break
            elif l1.val > l2.val:
                l_new.next = l2
                l_new = l_new.next
                l2 = l2.next
            else:
                l_new.next = l1
                l_new = l_new.next
                l1 = l1.next
        
        return pre.next
