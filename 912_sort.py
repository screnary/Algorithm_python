import pdb


class Solution:
    """ 912. 排序数组, ascending """
    def sortArray(self, nums):
        pass

    def count_sort(self, nums):
        if len(nums)==0: return []
        n = len(nums)
        # compute min and max value
        _min = min(nums)
        _max = max(nums)
        # construct counting arr
        counts = [0] * (_max-_min+1)
        for num in nums:
            counts[num-_min] += 1
        # construct target sorted arr from conting arr
        j = 0
        for i in range(n):
            while counts[j]==0:
                j += 1  # skip zero count num
            nums[i] = _min + j
            counts[j] -= 1
        return nums

    def bubble_sort(self, nums):
        steady = False
        while not steady:
            steady = True
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    steady = False 
        return nums
    
    def insert_sort(self, nums):
        for i in range(1, len(nums)):
            cur = nums[i]
            j = i-1
            while j >= 0 and nums[j] > cur:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = cur
        return nums
    
    def shell_sort(self, nums):
        n = len(nums)
        gap = n // 2
        while gap >= 1:
            for i in range(gap, n):
                cur = nums[i]
                j = i-gap
                while j >=0 and nums[j] > cur:
                    nums[j+gap] = nums[j]
                    j -= gap
                nums[j+gap] = cur
            gap = gap // 2
        return nums
    
    def select_sort(self, nums):
        for i in range(len(nums)-1):
            min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            tmp = nums[i]
            nums[i] = nums[min]
            nums[min] = tmp
        return nums
    
    def quick_sort(self, nums, left, right):
        """ if left==right, return """
        if left < right:
            base = self.partition(nums, left, right)
            nums = self.quick_sort(nums, left, base-1)
            nums = self.quick_sort(nums, base+1, right)
        return nums

    def partition(self, nums, left, right):
        """ get the base position """
        base = nums[left]
        while left < right:
            while left < right and nums[right] >= base:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] < base:
                left += 1
            nums[right] = nums[left]
        nums[left] = base
        return left

    def heap_sort(self, nums):
        # construct heap
        for i in range(len(nums)//2-1, -1, -1):
            nums = self.heap_adjust(nums, i, len(nums))
        # adjust heap structure, and swap top and bottom
        for j in range(len(nums)-1, 0, -1):
            nums[j], nums[0] = nums[0], nums[j]
            nums = self.heap_adjust(nums, 0, j)
        return nums

    def heap_adjust(self, nums, idx, length):
        cur = nums[idx]
        k = idx*2+1
        while k < length:
            if k+1 < length and nums[k] < nums[k+1]:
                k += 1  # get the largest child
            if nums[k] > cur:
                nums[idx] = nums[k]  # if node.value < child.value, swap
                idx = k  # no need to swap here
                k = k*2+1
            else:
                k = k*2+1
                break
        nums[idx] = cur
        return nums
    
    def merge_sort(self, nums, left, right):
        # do nothing while left == right
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(nums, left, mid)
            self.merge_sort(nums, mid+1, right)
            self.merge(nums, left, mid, right)
        return nums
    
    def merge(self, nums, left, mid, right):
        n1 = mid - left + 1  # to cover all the numbers
        n2 = right - mid
        ln = []
        rn = []
        for i in range(0, n1):
            ln.append(nums[left + i])
        for j in range(0, n2):
            rn.append(nums[mid + 1 + j])
        
        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if ln[i] <= rn[j]:
                nums[k] = ln[i]
                i += 1
            else:
                nums[k] = rn[j]
                j += 1
            k += 1

        while i < n1:
            nums[k] = ln[i]
            k += 1
            i += 1
        while j < n2:
            nums[k] = rn[j]
            k += 1
            j += 1


if __name__ == '__main__':
    nums = [5,2,3,1,6]
    sol = Solution()
    print(nums, end='->')
    # nums_sorted = sol.quick_sort(nums, 0, len(nums)-1)
    res = nums[:]
    # nums_sorted = sol.merge_sort(nums, 0, len(nums)-1)
    # print(nums_sorted)
    # nums_sorted = sol.heap_sort(nums)
    nums_sorted = sol.count_sort(nums)
    print(nums)
    print(nums_sorted)
