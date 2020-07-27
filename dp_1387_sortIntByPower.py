"""我们将整数 x 的 权重 定义为按照下述规则将 x 变成 1 所需要的步数：

如果 x 是偶数，那么 x = x / 2
如果 x 是奇数，那么 x = 3 * x + 1
比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。

给你三个整数 lo， hi 和 k 。你的任务是将区间 [lo, hi] 之间的整数按照它们的权重 升序排序 ，如果大于等于 2 个整数有 相同 的权重，那么按照数字自身的数值 升序排序 。
请你返回区间 [lo, hi] 之间的整数按权重排序后的第 k 个数。
注意，题目保证对于任意整数 x （lo <= x <= hi） ，它变成 1 所需要的步数是一个 32 位有符号整数。
链接：https://leetcode-cn.com/problems/sort-integers-by-the-power-value

DP, compute and save smaller integer's power value, which can be used to compute larger value
DFS + Dict
S[n]: the power value of num n
S[n] = S[n*3 + 1], if n%2==1
     = S[n/2], if n%2==0
"""


class Solution:
    def getKth(self, lo, hi, k):
        """ input| lo: int, hi: int, k:int
           output| int """
        # init the states dict
        S_dict = {1:0, 2:1}

        def dfs(n):
            # update S_dict and output
            if n not in S_dict:
                if n % 2 == 0:
                    S_dict[n] = dfs(n/2) + 1
                elif n % 2 == 1:
                    S_dict[n] = dfs(n*3+1) + 1
            return S_dict[n]

        for n in range(lo, hi+1):
            dfs(n)
        res_list = sorted(range(lo, hi+1), key=lambda x: S_dict[x])
        # print(res_list)
        return res_list[k-1]


if __name__ == '__main__':
    lo = 7
    hi = 11
    k = 4
    sol = Solution()
    res = sol.getKth(lo, hi, k)
    print(res)
