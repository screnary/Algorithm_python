""" 并查集 查找冗余边 """

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_node = len(edges)+1
        parents = [i for i in range(num_node)]
        for edge in edges:
            s, t = edge  # start, target nodes

            set1 = self.find(s, parents)
            set2 = self.find(t, parents)

            if set1 == set2:
                # set corrupt
                return edge
            else:
                # union sets
                parents[set1] = set2
        return [0,0]  # not found
    
    def find(self, node, parents):
        while parents[node] != node:
            node = parents[node]
        return parents[node]
    