from ListNode import *

class Solution:
    def swapPairs(self, head):
        """
        input: ListNode
        output: ListNode
        """
        if (head is None) or (head.next is None):
            return head
        subList = self.swapPairs(head.next.next)
        next_node = head.next
        head.next.next = head
        head.next = subList
        return next_node


if __name__ == '__main__':
    """ 1,2,3,4 
        2,1,4,3
    """
    nums = '0123456'
    li = [int(c) for c in nums[::1]]
    head = genList(li)
    printList(head)
    sol = Solution()
    res = sol.swapPairs(head)
    printList(res)
