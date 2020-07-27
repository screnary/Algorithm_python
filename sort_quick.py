import pdb

class Solution:
    def sortArray(self, nums):
        # quick sort, in-place, search in [left, right]
        def quick_sort(nums, left, right):
            # print(left, right, nums)
            # pdb.set_trace()
            if left < right:
                pivot = partition(nums, left, right)  # operation
                quick_sort(nums, left, pivot-1)  # dive deeper
                quick_sort(nums, pivot+1, right)

        def partition(nums, left, right):
            # get the partition idx
            base = nums[left]
            while left < right:
                while (left < right) and (nums[right] >= base):
                    right -= 1  # stop when met smaller or equal val
                nums[left] = nums[right]
                while (left < right) and (nums[left] < base):
                    left += 1  # stop when met greater val
                nums[right] = nums[left]
            # when left == right, and nums[left]<=base
            nums[left] = base
            # pdb.set_trace()
            return left

        quick_sort(nums, 0, len(nums)-1)
        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [5,2,3,1]
    res = sol.sortArray(nums)
    print(nums)
