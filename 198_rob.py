"""
198, rob I
213, rob II, ring houses, only one of head or tail can be robbed, then, max(rob(nums[1:N]), rob(nums[0:N-1]))
"""

class Solution:
    def rob1_v1(self, nums):
        """ 
        input: nums: List[int]
        output: int
        """
        N = len(nums)
        if N < 1:
            return 0

        dp = [0 for _ in range(N+1)]
        dp[1] = nums[0]
        for i in range(2,N+1):  # max(don't rob N, rob N)
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[-1]

    def rob1(self, nums):
        """ 
        input: nums: List[int]
        output: int
        """
        N = len(nums)
        if N < 1:
            return 0

        dp, dp_pre = 0, 0
        for i in range(0,N):  # max(don't rob N, rob N)
            dp, dp_pre = max(dp, dp_pre+nums[i]), dp
        return dp

    def rob(self, nums):
        # rob II, ring houses
        if len(nums) == 1:
            return nums[0]

        def my_rob(nums):
            dp, dp_pre = 0, 0
            for i in range(len(nums)):
                dp, dp_pre = max(dp, dp_pre + nums[i]), dp
            return dp

        rob_head = my_rob(nums[:-1])
        rob_tail = my_rob(nums[1:])
        return max(rob_head, rob_tail)


if __name__ == '__main__':
    nums = [1,3,2]
    sol = Solution()
    res = sol.rob(nums)
    print(res)
