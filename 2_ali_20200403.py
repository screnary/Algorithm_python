""" climb mountain,
DFS
"""
import sys
MAX_INT = sys.maxsize


def dfs(grid, n, m, i, j, visited, min_dist, dist):
    visited[i*n + j] = True
    if i == n-1:  # terminate condition
        if min_dist > dist:
            min_dist = dist
        visited[i*n+j] = False
        return min_dist
    elif i >= 0 and (j >=0 and j < m):  # valid position
        # for reachable next position
        for delta in check_space(grid, n, m, i, j):
            next_i = i + delta[0]
            next_j = j + delta[1]
            if visited[next_i*n + next_j]:
                # skip pre node
                continue
            min_dist = dfs(grid, n, m, next_i, next_j, visited, min_dist, dist+grid[next_i][next_j])
            # if cannot achieve goal, back to (i,j)
            visited[next_i*n + next_j] = False
        visited[i*n + j] = False  # finish search of pos (i,j), back to pre
    return min_dist


def check_space(grid, n, m, i, j):
    """ check the next possible position """
    # next move searching space:
    move = {'left':(0,-1), 'right':(0,1), 'up':(-1,0), 'down':(1,0)}
    # boundary check:
    if i==n-1:
        return []
    if i==0 and j==0:
        return [move['right'], move['down']]
    elif i==0 and j==m-1:
        return [move['left'], move['down']]
    elif i==0 and j>0 and j<m-1:
        return [move['left'], move['right'], move['down']]
    elif i>0 and j==0:
        return [move['up'], move['down'], move['right']]
    elif i>0 and j==m-1:
        return [move['up'], move['down'], move['left']]
    elif i>0 and j>0 and j<m-1:
        return list(move.values())


if __name__ == '__main__':
    # input
    # n, m = map(int, input().split(' '))
    # grid = [list(map(int, input().split(" "))) for _ in range(n)]
    
    # test input
    n, m = 3, 3
    grid = [[3,1,3],
            [3,1,0],
            [3,1,3]]

    visited = [False] * (n*m)
    min_dist = MAX_INT
    for i in range(m):
        cur_min = MAX_INT
        cur_min = dfs(grid, n, m, 0, i, visited, cur_min, grid[0][i])
        if min_dist > cur_min:
            min_dist = cur_min
    print(min_dist)
