""" 马戏团人塔
有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。
出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。

先按照身高升序排序，当身高相等时，按照体重降序排序（因为严格要求上面的人要轻、矮），问题转化为在体重sorted arr中寻找最长递增子序列。
"""


class Solution:
    def bestSeqAtIndex(self, height, weight):
        """input| height: List[int], weight: List[int]
          output| int
        """
        idx_sorted = sorted(range(len(height)), key=lambda x: (height[x], -weight[x]))
        weight_sorted = [weight[idx] for idx in idx_sorted]

        # find the longest increasing sub-sequence in weight_sorted, dynamic programing
        # ! time too long
        # dp[i], 以第i个元素结尾的最长子序列，需要遍历 j<i 来获取最大的 dp[j]，获得 dp[i]=dp[j]+1，O(n^2)
        dp = [0] * len(weight_sorted)
        dp[0] = 1
        max_ans = 0
        for i in range(1, len(weight_sorted)):
            max_val = 0
            for j in range(i):
                if weight_sorted[i] > weight_sorted[j]:
                    max_val = max(dp[j], max_val)
            dp[i] = max_val + 1
            max_ans = max(dp[i], max_ans)
        return max_ans
    
    def bestSeqAtIndex_bisect(self, height, weight):
        """input| height: List[int], weight: List[int]
          output| int
        """
        idx_sorted = sorted(range(len(height)), key=lambda x: (height[x], -weight[x]))
        weight_sorted = [weight[idx] for idx in idx_sorted]

        # find the longest increasing sub-sequence in weight_sorted, dynamic programing
        # d[i], 长度为 i 的最长上升子序列的末尾元素最小值，因为dp数组单调性，可以用二分查找优化向前查找时间 O(n*logn)
        # 找到 d 中小于 num 的最大数下标 k，将 d[k+1] = num
        d = []
        for num in weight_sorted:
            if not d or d[-1] < num:
                d.append(num)
            else:
                # bisection searching
                l, r = 0, len(d)-1
                while l <= r:
                    mid = (l+r) // 2
                    if d[mid] == num:
                        r = mid-1  # search for the left boundary in [l, r]
                    elif d[mid] > num:
                        r = mid-1
                    elif d[mid] < num:
                        l = mid+1
                d[l] = num  # update the d[l], because d[l-1] is the largest < num
        return len(d)


if __name__ == "__main__":
    sol = Solution()

    # height = [65,70,56,75,60,68]
    # weight = [100,150,90,190,95,110]
    height = [2868,5485,1356,1306,6017,8941,7535,4941,6331,6181]
    weight = [5042,3995,7985,1651,5991,7036,9391,428,7561,8594]
    res = sol.bestSeqAtIndex(height, weight)
    print(res)
