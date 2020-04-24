"""
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""

from ListNode import *

class Solution:
    def reverseList_recursive(self, head):
        """ input: ListNode
            output: ListNode
        """
        if head is None or head.next is None:
            return head
        cur = self.reverseList_recursive(head.next)
        # in the inner most loop, cur is tail
        head.next.next = head
        # unlink head and head.next, prevent loop list
        head.next = None
        # in every loop, cur is not updated, just record the tail
        return cur

    def reverseList_iter(self, head):
        pre = None
        cur = head
        while cur is not None:
            # record next node before change link
            next_tmp = cur.next
            cur.next = pre
            # shift pointers to 1 step right
            pre = cur
            cur = next_tmp
        return pre


if __name__ == '__main__':
    nums = '0123456'
    li = [int(c) for c in nums[::1]]
    head = genList(li)
    printList(head)
    sol = Solution()
    list_reversed = sol.reverseList_iter(head)
    printList(list_reversed)
    list_reversed_2 = sol.reverseList_recursive(list_reversed)
    printList(list_reversed_2)
