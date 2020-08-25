""" 递增子序列
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
1. find sub sequences: dfs
2. remove repeated, hash set
"""
import pdb


class Solution:
    def findSubsequences(self, nums):
        """ input| nums: List[int]
           output| List[List[int]]
        """
        memo = set()
        n = len(nums)
        res = []

        def dfs(st, path):
            # st: start location; path: record selection
            # update the res
            sid = ",".join(str(num) for num in path)
            if len(path) >=2 and sid not in memo:
                memo.add(sid)
                res.append(path.copy())
            for i in range(st, n):
                # search in the rest
                if len(path)==0 or (path[-1] <= nums[i]):
                    # make choice
                    path.append(nums[i])
                    # print(st, i, path)
                    # pdb.set_trace()
                    # only in this condition, need dfs
                    dfs(i+1, path)  # this start, should be i + 1, not st + 1
                    # cancel choice
                    path.pop()

        dfs(0, [])
        return res


if __name__ == "__main__":
    app = Solution()
    nums = [4,2,7,7]
    res = app.findSubsequences(nums)
    print(res)
