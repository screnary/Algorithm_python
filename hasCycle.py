# Definition for singly-linked list.
import pdb

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        hash
        76/52 ms
        17.5 MB
        maintain an address (or uniqe ID) lookup table
        """
        if not head:
            return False
        lookup = set()
        pdb.set_trace()
        while head:
            if id(head) in lookup:
                return True
            lookup.add(id(head))
            head = head.next
        return False

    def hasCycle_2p(self, head: ListNode) -> bool:
        """
        52 ms
        16.9 MB
        two speed pointers, chasing problem
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def hasCycle_setnone(self, head: ListNode) -> bool:
        """
        hash
        60 ms
        16.9 MB
        """
        if not head:
            return False
        while head.next and head.val != None:
            head.val = None
            head = head.next
            if not head:
                return False
        return True


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
    app = Solution()
    num1 = '34'
    num2 = '789012'
    l1 = [int(c) for c in num1[::1]]
    l2 = [int(c) for c in num2[::1]]
    a = genList(l1)
    b = genList(l2)
    printList(a)
    printList(b)
    print(a.next.next)
    print(app.hasCycle(b))
