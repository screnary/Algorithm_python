"""
Longest Increasing Subsequence
给定一个无序的整数数组，找到其中最长上升子序列的长度。
1,DP
dp[i]: 以 nums[i] 为结尾的子序列，的最大长度
dp[i+1] = max(dp[k])+1, k<i
dp[0] = 1
"""

class Solution:
    def lengthOfLIS(self, nums):
        """ input| nums: List[int]
           output| int
        """
        n = len(nums)
        if n==0:
            return 0
        dp = [0] * n
        dp[0] = 1
        max_len = 1
        for i in range(1, n):
            max_val = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_val = max(max_val, dp[j])
            dp[i] = max_val + 1
            max_len = max(max_len, dp[i])
        return max_len
    
    def lengthOfLIS_bisec(self, nums):
        """ input| nums: List[int]
           output| int
        """
        n = len(nums)
        if n==0:
            return 0
        # d[i], 长度为 i 的最长上升子序列的末尾元素最小值，因为dp数组单调性，可以用二分查找优化向前查找时间 O(n*logn)
        # 找到 d 中小于 num 的最大数下标 k，将 d[k+1] = num
        d = []

        for i in range(n):
            cur_num = nums[i]
            if not d or cur_num > d[-1]:
                d.append(cur_num)
            else:
                # 二分查找左侧最大的数<target
                l, r = 0, len(d)
                while l < r:
                    mid = (l+r) // 2
                    if d[mid] == cur_num:
                        r = mid
                    elif d[mid] > cur_num:
                        r = mid
                    elif d[mid] < cur_num:
                        l = mid+1
                d[l] = cur_num
        return len(d)
