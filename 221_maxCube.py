""" 221, 中等难度
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
Dynamic Programing
"""
import pdb


class Solution:
    def maximalSquare(self, matrix):
        """
        input: matrix: List[List[str]]
        output: int
        """
        if len(matrix)==0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        # dp[i][j]= max matrix side length, in range (<=i, <=j)
        max_side = 0
        # pdb.set_trace()
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(min(dp[i-1][j], dp[i-1][j-1]), dp[i][j-1]) + 1
                    if max_side < dp[i][j]:
                        max_side = dp[i][j]
        return max_side**2


if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    app = Solution()
    area = app.maximalSquare(matrix)
    print(area)
