"""
逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。
Divide conquer
merge sort

若在后有序数组元素出列时计算：
前有序数组非空，且后有序数组由元素出列时，计算逆序对=前有序数组剩余元素个数

若在前有序数组元素出列时计算：
后有序数组的当前 指针j-mid：为当前出列的left数组元素的逆序对（右边有多少个比他小的）。
"""

class Solution:
    def reversePairs(self, nums):
        """ input| nums: List[int]
           output| int
        """
        self.res = 0
        temp = [0] * len(nums)
        self.merge_sort_count(nums, 0, len(nums)-1, temp)
        return self.res
    
    def merge_sort_count(self, arr, left, right, temp):
        # temp is the same length as arr
        # res is an integer
        if left < right:  # right can be reached
            mid = (left + right) // 2
            self.merge_sort_count(arr, left, mid, temp)
            self.merge_sort_count(arr, mid+1, right, temp)
            # post order processing
            # while the left and right partials both sorted
            self.merge_count_inv(arr, left, mid, right, temp)
    
    def merge_count_inv(self, arr, left, mid, right, temp):
        for i in range(left, right+1):
            temp[i] = arr[i]
        i, j = left, mid+1
        for k in range(left, right+1):
            if i > mid:
                arr[k] = temp[j]
                j += 1
            elif j > right:
                arr[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            elif temp[i] > temp[j]:
                arr[k] = temp[j]
                self.res += (mid - i + 1)
                j += 1

    def sort_arr(self, nums):
        # merge sort
        temp = [0] * len(nums)
        self.merge_sort(nums, 0, len(nums)-1, temp)
        return nums

    def merge_sort(self, arr, left, right, temp):
        # temp is the same length as arr
        if left < right:  # right can be reached
            mid = (left + right) // 2
            self.merge_sort(arr, left, mid, temp)
            self.merge_sort(arr, mid+1, right, temp)
            # post order processing
            # while the left and right partials both sorted
            self.merge(arr, left, mid, right, temp)
    
    def merge(self, arr, left, mid, right, temp):
        for i in range(left, right+1):  # temp buffer
            temp[i] = arr[i]
        i, j = left, mid+1  # left, right start ptr
        for k in range(left, right+1):
            if i > mid:
                arr[k] = temp[j]
                j += 1
            elif j > right:
                arr[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            elif temp[i] > temp[j]:
                arr[k] = temp[j]
                j += 1
