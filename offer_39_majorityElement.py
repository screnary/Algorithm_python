""" 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。"""

class Solution:
    def majorityElement(self, nums):
        """ input| nums: List[int]
            output| int
        """
        # array sortting
        nums.sort()
        n = len(nums)
        half_l = n//2
        # return the middel of sorted array
        return nums[half_l]
