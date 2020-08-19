"""输入一个整型数组，数组里有正数也有负数。
数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
DP:
s[i]: 以第i个数结尾，子数组的最大和
s[i+1] = max(s[i]+nums[i+1], nums[i+1])
"""

class Solution():
    def maxSubArray(self, nums):
        """ input| nums: List[int]
           output| int
        """
        n = len(nums)
        dp = [-100] * n  # can be set to be an int
        dp[0] = nums[0]
        res = -100
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
        return res
