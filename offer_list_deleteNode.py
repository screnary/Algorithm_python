""" 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head, val):
        """ input| head: ListNode, val: int
           output| ListNode
        """
        dum = ListNode(0)
        dum.next = head
        pre = dum
        cur = head
        while cur is not None:
            if cur.val != val:
                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                break
        return dum.next            
