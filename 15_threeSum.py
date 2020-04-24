""" 
15, three sum
sort + two pointers
"""
import pdb

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        res = []
        k = 0
        nums.sort()
        for k in range(len(nums)-2):  # left=k+1<len(nums), and left<right<=len(nums)-1
            if nums[k] > 0:
                break
            if k>0 and nums[k]==nums[k-1]:
                continue
            left = k+1
            right = len(nums)-1
            while left<right:
                s = nums[k] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[k], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]: left += 1
                    while left<right and nums[right] == nums[right+1]: right -= 1
                elif s > 0:
                    right -= 1
                    while left<right and nums[right] == nums[right+1]: right -= 1
                else:
                    left += 1
                    while left<right and nums[left] == nums[left-1]: left += 1
        return res

    def threeSum_v1(self, nums):
        """ two slow """
        sols = []
        nums.sort()
        for i in range(len(nums)-2):
            num = nums[i]
            sol = self.twoSum(nums[i+1:], -num)
            if len(sol)>0:
                sols.extend(sol)
        # print(sols)
        # pdb.set_trace()
        sols = self.deRepeat(sols)
        return sols

    def twoSum(self, nums, target):
        sol = []
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            j = hashmap.get(target-nums[i])
            if j is not None and j!=i:
                sol.append([-target, nums[i],nums[j]])
        return sol
    
    def deRepeat(self, sols):
        uni = [i for i in range(len(sols))]
        sol_sets = [set(sol) for sol in sols]
        for i in range(len(sols)):
            for j in range(i+1, len(sols)):
                if len(sol_sets[i] & sol_sets[j]) == len(sol_sets[i]) and (j in uni):
                    uni.remove(j)
                    # print(i, uni)
        return [sols[idx] for idx in uni]


if __name__ == '__main__':
    nums = [0,0,0]
    sol = Solution()
    res = sol.threeSum(nums)
    print(res)
