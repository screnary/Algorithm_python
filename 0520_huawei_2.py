# input is "A->B;B->D;C->B;C->E;D->C"
# process input, form a matrix grid (graph)
import pdb
def main():
    in_str = input()
    edges = in_str.split(";")
    graph = [[0] * 10 for _ in range(10)]  # 10*10 matrix
    for e in edges:
        s, t = ord(e[0])-ord("A"), ord(e[-1])-ord("A")
        graph[s][t] = 1

    # dfs the graph
    visited = [False] * 10
    res = []

    def dfs(graph, i, path):
        # path is str recording the traverse route
        visited[i] = True
        for j in range(10):
            if graph[i][j] != 0:
                if not visited[j]:
                    dfs(graph, j, path+chr(ord("A") + j))
                    visited[j] = False
                elif visited[j]:
                    res.append(path)
                    return
    """ ! need compute the in-degree, then dfs all the 1-in-degree nodes """
    start = ord(in_str[0]) - ord('A')
    # need to dfs all the node, whose indegree==0
    dfs(graph, start, "")
    if res:
        string = res[0]
        minnode = string[0]
        minid = 0
        for i in range(len(string)):
            if string[i] < minnode:
                minnode = string[i]
                minid = i
        p_res = string + string

        print(p_res[minid: (minid + len(string))])

    else:
        print("-")


if __name__ == '__main__':
    main()
    