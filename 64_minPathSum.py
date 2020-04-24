""" 
64, min path sum.
each step: > or v.
DFS
DP
"""
import sys
MaxInt = sys.maxsize

class Solution:
    def minPathSum_dp(self, grid):
        """
        Dynamic Programing
        input: grid: List[List[int]]
        output: int 
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # traversing grid
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]

    def minPathSum_dp_opt(self, grid):
        """
        Dynamic Programing, once visited, left up grid not used anymore
        input: grid: List[List[int]]
        output: int 
        """
        m, n = len(grid), len(grid[0])
        # traversing grid
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[m-1][n-1]

    def minPathSum_dfs(self, grid):
        self.min_path = MaxInt
        self.dfs(grid, 0, 0, grid[0][0])
        return self.min_path

    def dfs(self, grid, i, j, dist):
        m, n = len(grid), len(grid[0])
        # terminal check
        if i == m-1 and j == n-1:
            # reach end
            if self.min_path > dist:
                self.min_path = dist
            return
        # searching space: {right, down}
        mov_r = [0, 1]  # [d_y, d_x]
        mov_d = [1, 0]  # [d_y, d_x]
        movs = [mov_r, mov_d]
        for mov in movs:
            next_i, next_j = i+mov[0], j+mov[1]
            if next_i < m and next_j < n:
                dist += grid[next_i][next_j]
                self.dfs(grid, i+mov[0], j+mov[1], dist)
                dist -= grid[next_i][next_j]
