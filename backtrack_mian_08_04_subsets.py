"""
输出无重复元素集合的幂集
"""

class Solution:
    def subsets(self, nums):
        n = len(nums)
        if n==0:
            return [[]]

        res = []
        visited = [False] * n
        def backtrack(path, start):
            nonlocal res
            # start is current depth of decision tree
            if start == n:
                res.append(path[:])  # deep copy
                return
            # left decision tree
            path.append(nums[start])
            backtrack(path, start+1)
            path.pop()
            # right decision tree
            backtrack(path, start+1)

        backtrack([], 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.subsets([1,2,3])
    print(res)
    print(len(res))
