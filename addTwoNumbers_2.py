# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    LeetCode No.445, add two numbers II
    88 ms,
    14 MB
    """
    @staticmethod
    def __getlen(l: ListNode) -> int:
        length = 0
        while l:
            length = length + 1
            l = l.next
        return length

    @staticmethod
    def __filllen(l: ListNode, n: int) -> ListNode:
        """ fill with n zeros, before the List """
        prenode = ListNode(0)
        lastnode = prenode
        for i in range(n):
            lastnode.next = ListNode(0)
            lastnode = lastnode.next
        lastnode.next = l
        return prenode.next

    def __addrec(self, l1: ListNode, l2: ListNode, l3: list) -> int:
        """ recursively add two List """
        if (l1 is None) and (l2 is None):
            return 0
        carry = self.__addrec(l1.next, l2.next, l3)
        val = (l1.val + l2.val + carry) % 10
        l3.append(val)
        return (l1.val + l2.val + carry) // 10

    @staticmethod
    def __genList(l: list) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode
        for val in l:
            lastnode.next = ListNode(val)
            lastnode = lastnode.next
        return prenode.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # compute List length
        len1 = self.__getlen(l1)
        len2 = self.__getlen(l2)
        if len1 < len2:
            l1, l2 = l2, l1  # keep l1 longer
            len1, len2 = len2, len1

        l2 = self.__filllen(l2, len1 - len2)
        self.res = []
        carry = self.__addrec(l1, l2, self.res)
        if carry != 0:
            self.res.append(carry)
        return self.__genList(self.res[::-1])


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
    num1 = '3'
    num2 = '7'
    l1 = [int(c) for c in num1[::1]]
    l2 = [int(c) for c in num2[::1]]
    a = genList(l1)
    b = genList(l2)
    printList(a)
    printList(b)
    printList(app.addTwoNumbers(a, b))

