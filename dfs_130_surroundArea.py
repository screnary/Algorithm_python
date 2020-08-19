""" 被围绕的区域
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

思路：
从四方边界 flood，flood的记为‘A’
最后再遍历数组来恢复

比较难想到的是，四方边界起始的flood搜索。
"""

import pdb

class Solution:
    def solve(self, board):
        """
        input| board: List[List[str]]
        Do not return anything, modify board in-place instead
        """
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])  # m row, n col

        def dfs(board, i, j):
            # terminate
            if i < 0 or i >=m or j < 0 or j >=n or board[i][j] != 'O':
                # out of range
                return
            # pre order mark
            board[i][j] = 'A'
            dfs(board, i+1, j)
            dfs(board, i-1, j)
            dfs(board, i, j+1)
            dfs(board, i, j-1)

        for i in range(m):
            dfs(board, i, 0)
            dfs(board, i, n-1)
        for j in range(n):
            dfs(board, 0, j)
            dfs(board, m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'

if __name__ == "__main__":
    board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    app = Solution()
    app.solve(board)
    print(board)
