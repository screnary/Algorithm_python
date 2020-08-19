class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash tabel, if do not use set(), O(n**2) 
        numset = set(nums)
        n = len(nums)
        for i in range(n):
            a = nums[i]
            # numset.remove(a)
            if (target-a) in numset:
                return [a, target-a]
            # else:
            #     numset.add(a)
        return []
    
    def twoSum_pointer(self, nums: List[int], target: int) -> List[int]:
        # double pointers
        s, t = 0, len(nums)-1
        while s < t:  # find two numbers, so valid s < t
            if nums[s] + nums[t] == target:
                return [nums[s], nums[t]]
            elif nums[s] + nums[t] > target:
                t -= 1
            elif nums[s] + nums[t] < target:
                s += 1
        return []
