"""
643
给定n个整数，找出平均数最大的，且长度为 k 的连续子数组
输出该最大平均数

滑动窗口，在于减少计算量
"""
import pdb

class Solution:
    def findMaxAverage(self, nums, k):
        if k > len(nums) or k==0:
            return 0

        total = sum(nums[0:k])
        maxsum = total
        for i in range(k, len(nums)):
            total -= nums[i-k]
            total += nums[i]
            maxsum = total if total > maxsum else maxsum
        return maxsum / k

    def findMaxAverage_bk(self, nums, k):
        # too slow
        s = 0
        sumval = float('-inf')
        while s+k <= len(nums):
            # pdb.set_trace()
            sub = nums[s:s+k]
            tmp = sum(sub)
            sumval = tmp if sumval < tmp else sumval

            s += 1
        return sumval / k
    
    def heap_top(self, arr):
        """ get the min heap top """
        k = len(arr)  # heap scale
        def sift_down(arr, root, k):
            cur_val = arr[root]
            while 2*root + 1 < k:
                child = 2*root + 1
                if child + 1 < k and arr[child+1] < arr[child]:
                    child = child + 1
                if arr[root] > arr[child]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = cur_val
        
        # sift down through out the array
        for root in range((k-2) // 2, -1, -1):
            sift_down(arr, root, k)
        
        return arr[0]



if __name__ == "__main__":
    nums = [8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891]
    k = 93
    sol = Solution()
    output = sol.findMaxAverage_bk(nums, k)
    print(output)
    print(sum(nums[-k:])/k)
    print(len(nums))
