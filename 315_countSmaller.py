"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

从右侧算起，右侧的count结果可以用于左侧的计算
递归
"""

class Solution:
    def countSmaller(self, nums):
        """
        divide conquer, mergesort, inverse count 
        """
        res = [0] * len(nums)
        index = [i for i in range(len(nums))]
        temp = [0] * len(nums)
        self.count_inv_num(nums, 0, len(nums)-1, temp, index, res)
        return res
    
    def count_inv_num(self, arr, left, right, temp, index, res):
        # if only one element
        if left == right:
            return
        if left < right:
            mid = left + (right-left)//2
            self.count_inv_num(arr, left, mid, temp, index, res)
            self.count_inv_num(arr, mid+1, right, temp, index, res)
            # until now, [left, mid] and [mid+1, right] have already computed inv_count, and sorted
            if arr[index[mid]] > arr[index[mid+1]]:
                self.merge_and_count(arr, left, mid, right, temp, index, res)
        
    def merge_and_count(self, arr, left, mid, right, temp, index, res):
        """ all changes occur to index, arr remains not changed """
        for i in range(left, right+1):
            temp[i] = index[i]
        i = left
        j = mid + 1
        for k in range(left, right+1):
            if i > mid:
                index[k] = temp[j]
                j += 1
            elif j > right:
                index[k] = temp[i]
                res[index[k]] += right - mid
                i += 1
            elif arr[temp[i]] <= arr[temp[j]]:
                index[k] = temp[i]
                res[index[k]] += (j - mid - 1)
                i += 1
            else:
                assert arr[temp[i]] > arr[temp[j]]
                # count the inversion num
                index[k] = temp[j]
                # res[index[k]] += (mid - i + 1)
                j += 1
    
    def merge_sort(self, arr, left, right, temp):
        """ l,r,mid can be reached by merge_sort 
            temp is the same length with arr
        """
        if left == right:
            pass
        if left < right:
            mid = left + (right-left)//2
            self.merge_sort(arr, left, mid, temp)
            self.merge_sort(arr, mid+1, right, temp)
            # to here, [left, mid] and [mid+1, right] all are ordered
            self.merge(arr, left, mid, right, temp)
    
    def merge(self, arr, left, mid, right, temp):
        for i in range(left, right+1):
            temp[i] = arr[i]
        i = left
        j = mid + 1
        for k in range(left, right+1):
            if i > mid:
                # left batch empty
                arr[k] = temp[j]
                j += 1
            elif j > right:
                # right batch empty
                arr[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                # pick form left batch
                arr[k] = temp[i]
                i += 1
            else:
                assert temp[i] > temp[j]
                # pick from right batch
                arr[k] = temp[j]
                j += 1
    
    def countSmaller_v1(self, nums):
        """ too slow
        O(n^2)
        """
        def counter(idx, arr):
            cur_val = arr[idx]
            num = 0
            if idx == len(arr)-1:
                return 0
            for i in range(idx+1, len(arr)):
                if arr[i] < cur_val:
                    num += 1
            return num

        counts = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            counts[i] = counter(i, nums)
        return counts


if __name__ == '__main__':
    nums = [5,2,6,1,3,7,0]
    sol = Solution()
    counts = sol.countSmaller(nums)
    print(counts)
    # temp = [0] * len(nums)
    # sol.merge_sort(nums, 0, len(nums)-1, temp)
    # print(nums)
