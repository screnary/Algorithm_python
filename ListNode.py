class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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