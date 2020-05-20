""" 不相交的线
我们在两条独立的水平线上按给定的顺序写下 A 和 B 中的整数。
现在，我们可以绘制一些连接两个数字 A[i] 和 B[j] 的直线，只要 A[i] == B[j]，且我们绘制的直线不与任何其他连线（非水平线）相交。
以这种方法绘制线条，并返回我们可以绘制的最大连线数。

状态：
dp[i][j]: A[i,...] 和 B[j, ...] 中的最大不相交线数目；目标是求 dp[0][0]
转移：
A[i]==B[j]时，
若连接，则 dp[i][j] = dp[i+1][j+1] + 1
若不连，则 dp[i][j] = max(dp[i][j+1], dp[i+1][j])
A[i]!=B[j],
dp[i][j] = max(dp[i][j+1], dp[i+1][j])
"""

class Solution:
    def maxUncrossedLines(self, A, B):
        """ input| A: List[int], B: List[int]
           output| int
        """
        m = len(A)
        n = len(B)
        dp = [[0] * (n+1) for _ in range(m+1)]  # m x n matrix
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
