""" 
912 排序数组,升序
"""
class Solution:
    def sortArray(self, nums):
        # nums: list[n]
        # return: list[n]
        # self.heap_sort(nums)
        # return nums
        temp = [0] * len(nums)
        self.merge_sort(nums, 0, len(nums)-1, temp)
        return nums
    
    def heap_sort(self, arr):
        # ascend
        k = len(arr)  # scale of heap
        assert k >= 1
        def sift_down(arr, root, k):
            cur_val = arr[root]
            while 2*root + 1 < k:
                child = 2*root + 1
                if child+1 < k and arr[child] < arr[child+1]:
                    child = child+1
                if cur_val < arr[child]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = cur_val
        
        # create heap
        for root in range((k-2)//2, -1, -1):
            sift_down(arr, root, k)
        
        # sort
        for s in range(k-1, 0, -1):
            arr[0], arr[s] = arr[s], arr[0]
            sift_down(arr, 0, s)
    
    def merge_sort(self, arr, left, right, temp):
        """
        left: left boundary, can reach
        right: right boundary, can reach
        temp: same size with arr, assistant arr in __merge()
        """
        if left == right:  # only has one element
            return
        if left < right:
            mid = left + (right-left)//2
            self.merge_sort(arr, left, mid, temp)
            self.merge_sort(arr, mid+1, right, temp)
            if arr[mid] <= arr[mid+1]:
                return
            self.__merge(arr, left, mid, right, temp)
    
    def __merge(self, arr, left, mid, right, temp):
        for i in range(left, right+1):
            temp[i] = arr[i]
        l = left
        r = mid + 1
        for k in range(left, right+1):
            if l > mid:
                arr[k] = temp[r]
                r += 1
            elif r > right:
                arr[k] = temp[l]
                l += 1
            elif temp[l] <= temp[r]:
                arr[k] = temp[l]
                l += 1
            else:
                assert temp[l] > temp[r]
                arr[k] = temp[r]
                r += 1
