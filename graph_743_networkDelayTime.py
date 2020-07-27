from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        """ input| times: List[List[int]], N: int, K: int
           output| int
        """
        # Dijkstra
        # init graph
        graph = defaultdict(dict)
        for time in times:
            u, v, w = time
            graph[u][v] = w
        q = [(0, K)]  # source node inqueue, heap
        visited = set()  # source set
        # borad first search
        while q:
            time, node = heapq.heappop(q)
            visited.add(node)
            if len(visited) == N:
                return time
            for nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(q, (time + graph[node][nei], nei))
        if len(visited) < N:
            return -1
