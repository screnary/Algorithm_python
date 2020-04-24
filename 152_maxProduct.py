""" 
152, 乘积最大的连续子数组
DP
"""

class Solution:
    def maxProduct(self, nums):
        """ 状态压缩 """
        N = len(nums)
        maxPro = nums[0]
        if N==1: return maxPro

        maxDP = nums[0]
        minDP = nums[0]
        for i in range(1, N):
            temp = maxDP  # for minDP compute, after update maxDP
            maxDP = max(max(nums[i], maxDP * nums[i]), minDP * nums[i])
            minDP = min(min(nums[i], minDP * nums[i]), temp * nums[i])
            maxPro = max(maxPro, maxDP)
        return maxPro

    def maxProduct_force(self, nums):
        """ O(N^2)
        input:
            nums: List[int]
        output:
            res: int
        """
        N = len(nums)
        maxPro = nums[0]
        if N == 1:
            return maxPro
        for i in range(N):
            tempPro = nums[i]
            for j in range(i,N):
                if i==j:
                    pass
                else:
                    tempPro *= nums[j]
                if maxPro < tempPro:
                    maxPro = tempPro
        return maxPro


if __name__ == '__main__':
    nums = [2,3,-2,4]
    sol = Solution()
    res = sol.maxProduct(nums)
    print(res)
