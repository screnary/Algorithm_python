# undirected graph, find the neighbors within the distance threshold; Then return the node with least neighbors
from collections import defaultdict


class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        """ input| n: int, edges: List[List[int]], distanceThreshold: int
           output| int
        """
        # init the undirected graph
        graph = [[100000] * n for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0
        for edge in edges:
            s, t, w = edge
            graph[s][t] = w
            graph[t][s] = w

        # compute min dist between all nodes
        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        # output
        min_nei = n
        min_node = 0
        for i in range(n):
            cur_nei = 0
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    cur_nei += 1
            if cur_nei <= min_nei:
                min_nei = cur_nei
                min_node = i

        return min_node
