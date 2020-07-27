import pdb

class Solution:
    def gardenNoAdg(self, N, paths):
        """ input| N: int, paths: list[int]
           output| res: List[int]
        """
        # get adjacent dict, graph={node:[neighbors]}
        graph = {i+1:[] for i in range(N)}
        for edge in paths:
            st, ed = edge
            # two-way path
            graph[st].append(ed)
            graph[ed].append(st)
        # paint from larger degree gardens
        nodes = sorted(graph, key=lambda x: len(graph[x]), reverse=True)
        planted = [0] * (N+1)
        for node in nodes:
            # init color set
            color = [1,2,3,4]
            # check neighbors
            # pdb.set_trace()
            for nei in graph[node]:
                if planted[nei] in color:
                    color.remove(planted[nei])
            # we know that, node must can be colored
            planted[node] = color[0]
        return planted[1:]


if __name__ == '__main__':
    sol = Solution()
    N = 3
    paths = [[1,2],[2,3],[3,1]]
    res = sol.gardenNoAdg(N, paths)
    print(res)
