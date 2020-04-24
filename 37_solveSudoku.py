""" 
37. Sove Sudoku
Depth First Searching
36. is valid Sudoku
"""
class Solution:
    def __init__(self):
        self.sub_n = 3  # sub region size
        self.N = self.sub_n ** 2  # whole region size=9
        # maintain the rules: rows, cols, and sub cubes (blocks)
        self.rule_rows = [set() for _ in range(self.N)]
        self.rule_cols = [set() for _ in range(self.N)]
        self.rule_cubes = [set() for _ in range(self.N)]

        self.solved = False  # solution flag
    
    def __notoccupied(self, d, i, j):
        return (d not in self.rule_rows[i]) and (d not in self.rule_cols[j]) and (d not in self.rule_cubes[(i//3)*3 + j//3])

    def set_final_grid(self, board, d, i, j):
        if i == self.N-1 and j == self.N-1:  # i==j==8
            # process the final grid
            if board[i][j] is ".":
                if self.__notoccupied(d, i, j):
                    board[i][j] = str(d)  # put d at (i,j)
                    self.rule_rows[i].add(d)
                    self.rule_cols[j].add(d)
                    self.rule_cubes[(i//3)*3 + j//3].add(d)
                    self.solved = True
            else:
                self.solved = True
            return

    def dfs(self, board, i, j):
        """ solve the (i,j)th grid on the Sudoku board,
        and go on based on that.
        """
        # 1, put a number on space grid
        # print(i, j)
        # if j == 8:
        #     pdb.set_trace()
        if board[i][j] is ".":
            for d in range(1,10):
                if self.__notoccupied(d, i, j):
                    board[i][j] = str(d)  # put d at (i,j)
                    self.rule_rows[i].add(d)
                    self.rule_cols[j].add(d)
                    self.rule_cubes[(i//3)*3 + j//3].add(d)
                    # move on to next grid
                    if j < self.N - 1:
                        self.dfs(board, i, j+1)  # fill from the right grid
                    elif i < self.N - 1:  # j==8, i < 8
                        assert j==8
                        self.dfs(board, i+1, 0)  # fill from the next line
                    else:
                        assert i==8 and j==8
                        self.set_final_grid(board, d, i, j)
                    # check sucess or not
                    if not self.solved:
                        # if not reach bottom-right grid
                        self.rule_rows[i].remove(d)
                        self.rule_cols[j].remove(d)
                        self.rule_cubes[(i//3)*3 + j//3].remove(d)
                        board[i][j] = "."
        else:
            if j < self.N - 1:
                self.dfs(board, i, j+1)
            elif i < self.N - 1:
                self.dfs(board, i+1, 0)
            else:
                assert i == 8 and j == 8
                self.solved = True
                return
            return  # back to upper dfs

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        input: board: List[List[str]]
        """
        for i in range(0, self.N):
            for j in range(0, self.N):
                if board[i][j] is not ".":
                    d = int(board[i][j])
                    self.rule_rows[i].add(d)
                    self.rule_cols[j].add(d)
                    self.rule_cubes[(i//3)*3 + j//3].add(d)
        
        self.dfs(board, 0, 0)
    
    def isValidSudoku(self, board):
        """ return bool """
        valid = True
        for i in range(0, self.N):
            for j in range(0, self.N):
                if board[i][j] is not ".":
                    d = int(board[i][j])
                    if self.__notoccupied(d, i, j):
                        self.rule_rows[i].add(d)
                        self.rule_cols[j].add(d)
                        self.rule_cubes[(i//3)*3 + j//3].add(d)
                    else:
                        valid = False
                        return valid
        return valid


if __name__ == '__main__':
    board= [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

    sol = Solution()
    print(sol.isValidSudoku(board))
    sol.solveSudoku(board)
    print(board)
