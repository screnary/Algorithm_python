"""
25. reverse k group listNode
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        input:
            head: ListNode
            k: int
        return:
            ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        end = dummy
        while(end != None):
            for _ in range(k):
                if end != None:
                    end = end.next
            if end == None:  # reach tail
                break
            start = pre.next
            next_head = end.next
            end.next = None  # unlink
            pre.next = self.reverse(start)  # dummy.next=reversed
            start.next = next_head

            pre = start
            end = pre

        return dummy.next
    
    def reverse(self, head):
        pre = None
        cur = head
        while cur is not None:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre


def genList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l: ListNode):
    outstr = ''
    while l:
        outstr = outstr + str(l.val)
        l = l.next
        if l:
            outstr = outstr + ' -> '
    print(outstr)


if __name__ == '__main__':
    num2 = '123456789'
    l2 = [int(c) for c in num2[::1]]
    b = genList(l2)
    printList(b)

    sol = Solution()
    b_revk = sol.reverseKGroup(b,4)
    printList(b_revk)
