"""
关键点：同时检测是否有环，并更新排序。图的构建，要考虑没有边的孤立节点！
"""

from collections import defaultdict
import pdb

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """ input| numCourses: int, prerequisites: List[List[int]]
           output| List[int] """
        graph = defaultdict(list)
        for edge in prerequisites:
            tar, pre = edge
            graph[pre].append(tar)
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
        # pdb.set_trace()
        
        visited = [0] * numCourses
        order = [-1] * numCourses
        invalid = False
        def dfsTopsort(v, visited, order, n):
            nonlocal invalid

            if n < 0:  # used up all the n
                return n
            if visited[v] == 2:  # skip finished vertex
                return n

            # start searching from this vertex
            visited[v] = 1
            for nei in graph[v]:
                if visited[nei]==0:
                    n = dfsTopsort(nei, visited, order, n)
                    if invalid:
                        return -1
                elif visited[nei]==1:
                    # detect cycle while searching
                    invalid = True
                    return -1

            order[n] = v
            
            # pdb.set_trace()
            visited[v] = 2  # finished sorting this vertex
            # print(v, order, "visited: ", visited, "returned: ", n-1)
            return n-1

        # print(graph.items())
        n = numCourses - 1
        for v in graph:
            # print("from vertex: ", v)
            n = dfsTopsort(v, visited, order, n)

        if invalid:
            return []
        return order

    def canFinish(self, numCourses, prerequisites):
        """ output| bool (if valid) """
        graph = defaultdict(dict)
        for edge in prerequisites:
            pre, tar = edge
            graph[pre][tar] = True

        visited = [0] * numCourses
        def dfs(graph, v):
            if visited[v]==1:
                # has cycle
                return False
            if visited[v]==-1:  # visited but has no cycle
                return True
            # visit this node
            visited[v] = 1
            # dfs traverse
            for nei in graph[v]:
                if not dfs(graph, nei):
                    return False
            # reset this node
            visited[v] = -1  # visited but has no cycle
            return True
        
        for i in range(numCourses):
            if not dfs(graph, i):
                return False  # note that, dfs should have return value
        return True


if __name__ == "__main__":
    app = Solution()
    numCourses = 3
    prerequisites = [[1,0]]
    res = app.findOrder(numCourses, prerequisites)
    print(res)
