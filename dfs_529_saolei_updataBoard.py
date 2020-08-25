""" 529. 扫雷游戏
给定一个代表游戏板的二维字符矩阵。 
'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，
'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，
'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。

[wzj, 2020/08/20]
难点在于，每个分支需要return什么？return之后到了哪个递归层级，是否会走入死胡同。
这里进行 inplace 修改，所以最后返回 board 就好
遇到相邻区域有地雷的区域，标注该区域为数字，这时不再递归搜索该区域了，返回到上个层级。
"""

class Solution:
    def updataBoard(self, board, click):
        """ input| board: List[List[str]], click: List[int]
           output| List[List[int]]
        """
        m, n = len(board), len(board[0])
        if board[click[0]][click[1]] == 'M':
            # gameover
            board[click[0]][click[1]] = 'X'
            return board

        offsets = [[0,1], [0,-1],
                   [1,0], [-1,0],
                   [1,1], [1,-1],
                   [-1,1], [-1,-1]]
        def checkAround(board, pos):
            # check if adjacent to mines
            res = 0
            for offset in offsets:
                di, dj = offset[0], offset[1]
                i = pos[0] + di
                j = pos[1] + dj
                if (i < 0 or i >= m) or (j < 0 or j >= n):
                    continue
                if board[i][j] == 'M':
                    res += 1
            return res

        def dfs(board, pos):
            # pos = [i, j]
            # terminate condition
            
            i, j = pos[0], pos[1]
            if (i < 0 or i >= m) or (j < 0 or j >= n):
                # out of range, do nothing here, return to outter loop
                return
            # print(i, j, board[i][j])
            if board[i][j] == 'M':
                # found a mine, do nothing here, return to outter loop
                return
            if board[i][j] == 'E':
                count = checkAround(board, pos)
                if count:
                    # found mines in neighborhood
                    board[i][j] = str(count)  # change mark
                    return  # return to outter loop
                else:
                    # if is not adjacent to a mine
                    for offset in offsets:
                        board[i][j] = 'B'  # change mark
                        # print(i, j, board[i][j])
                        di, dj = offset[0], offset[1]
                        dfs(board, [pos[0]+di, pos[1]+dj])

        dfs(board, click)
        return board


if __name__ == "__main__":
    board = [['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'M', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E']]
    click = [3,0]
    app = Solution()
    res = app.updataBoard(board, click)
    print(res)
