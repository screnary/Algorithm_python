""" 岛屿最大面积
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        """ input| grid: List[List[int]]
           output| max_area: int
        """
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def dfs(grid, visited, i, j):
            """ dfs region grow """
            nonlocal area
            # terminate condition
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return
            if grid[i][j]==0 or visited[i][j]==True:
                return
            
            # operation this location
            visited[i][j] = True
            area += 1
            # traverse deeper
            dfs(grid, visited, i+1, j)
            dfs(grid, visited, i-1, j)
            dfs(grid, visited, i, j+1)
            dfs(grid, visited, i, j-1)
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]==1:
                    area = 0
                    dfs(grid, visited, i, j)
                    max_area = max(max_area, area)
        return max_area
