# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    LeetCode No.2, add two numbers
    76 ms,
    13.8 MB
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        prenode = ListNode(0)
        lastnode = prenode
        while carry or l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            lastnode.next = ListNode(val)
            lastnode = lastnode.next

            l1 = l1.next if l1 else None  # shift to next node
            l2 = l2.next if l2 else None
        return prenode.next


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
    num1 = '123'
    num2 = '4567'
    l1 = [int(c) for c in num1[::-1]]
    l2 = [int(c) for c in num2[::-1]]
    a = genList(l1)
    b = genList(l2)
    printList(a)
    printList(b)
    printList(app.addTwoNumbers(a, b))
