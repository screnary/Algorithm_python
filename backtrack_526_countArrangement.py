""" 优美的排列 
假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，
使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

1) 第 i 位的数字能被 i 整除
or 2) i 能被第 i 位上的数字整除
现在给定一个整数 N，请问可以构造多少个优美的排列？

注意！ 用 self 变量，会慢很多
"""

class Solution():
    def countArrangement(self, N):
        """
        input:      N: int
        return:     int
        """
        self.res = 0
        self.N = N
        self.used = [False] * (N+1)

        def isBeauty(x, y):
            return (x % y)==0 or (y % x)==0

        def backtrack(trace):
            # trace is the position of the decision path
            if trace == self.N:
                self.res += 1
            for num in range(1, self.N+1):
                if not self.used[num] and isBeauty(num, trace+1):
                    self.used[num] = True
                    trace = trace + 1
                    backtrack(trace)
                    self.used[num] = False
                    trace = trace - 1

        backtrack(0)
        return self.res
