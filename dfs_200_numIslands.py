""" 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

使用深度优先搜索，dfs 区域增长
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ input| grid: List[List[str]]
           output| int
        """
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        res = 0

        def dfs(grid, visited, i, j):
            """ dfs region grow """
            # terminate condition
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
                return
            if grid[i][j]=="0" or visited[i][j]:
                return

            # operate this position
            visited[i][j] = True

            # traverse deeper in choice list
            dfs(grid, visited, i+1, j)
            dfs(grid, visited, i-1, j)
            dfs(grid, visited, i, j+1)
            dfs(grid, visited, i, j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=="1":
                    dfs(grid, visited, i, j)
                    res += 1
        return res
