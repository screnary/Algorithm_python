from collections import defaultdict
import heapq
import math


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """ input| n: int, edges: List[List[int]], succProb: List[float], start: int, end: int
            output| float """
        # construct nondirection graph
        graph = defaultdict(dict)
        for i, edge in enumerate(edges):
            prob = succProb[i]
            s, t = edge
            graph[s][t] = prob
            graph[t][s] = prob
        q = [(0, start)]  # (dist=-log(prob), node), the Source Set in Dijkstra algorithm
        visited = {start}
        while q:
            prob, node = heapq.heappop(q)
            if node == end:
                return math.exp(-prob)
            visited.add(node)
            for nxt in graph[node]:
                if nxt not in visited:
                    heapq.heappush(q, (prob - math.log(graph[node][nxt]), nxt))  # dist[node] + dist[node][nxt] as dist[nxt]
        return 0
