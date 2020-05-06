"""
并查集 + 分类讨论（节点入度）
"""

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for i in range(len(edges)):
            nodes.add(edges[i][0])
            nodes.add(edges[i][1])
        N = len(nodes)
        parents = [i for i in range(N+1)]  # dui qi index and Node
        indegrees = [0] * (N+1)  # compute the indegree for each node
        for edge in edges:
            s, t = edge
            indegrees[t] += 1
        if 2 in indegrees:
            dual_node = indegrees.index(2)
            dual_edges = []
            for edge in edges:
                s, t = edge
                if t == dual_node:
                    dual_edges.append(edge)
            # check and del from the tail of edges chart
            for edge in dual_edges[::-1]:
                has_cycle = False
                for e in edges:
                    if e != edge:
                        if self.union(e[0], e[1], parents):
                            has_cycle = True
                if has_cycle:  # del edge, still has cycle
                    return dual_edges[0]
                else:
                    return edge
        else:
            for edge in edges:
                s, t = edge
                red_edge = self.union(s, t, parents)
                if red_edge:
                    return red_edge                  
    
    def find(self, node, parents):
        while parents[node] != node:
            node = parents[node]
        return parents[node]
    
    def union(self, node1, node2, parents):
        root1 = self.find(node1, parents)
        root2 = self.find(node2, parents)
        if root1 == root2:
            return [node1, node2]
        else:
            parents[root2] = root1  # set to be node1's root (root1->node1->node2)