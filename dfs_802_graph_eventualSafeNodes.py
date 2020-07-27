class Solution:
    def eventualSafeNodes(self, graph):
        """ input: graph: List[List[int]]
            output: List[int]
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        color = [0] * len(graph)

        def dfs(node):
            # terminate condition
            if color[node] != WHITE:
                # if this node has been visited
                return color[node] == BLACK
            
            # visit this node
            color[node] = GRAY

            # search deeper
            for next_node in graph[node]:
                if color[next_node] == BLACK:
                    continue  # search for next neighbor
                if color[next_node] == GRAY:
                    return False  # next node has been visited
                if not dfs(next_node):
                    return False  # from next node, result in cycle
            color[node] = BLACK
            return True  # this node is safe
        
        for i in range(len(graph)):
            dfs(i)
        res = []
        for i in range(len(color)):
            if color[i]==BLACK:
                res.append(i)
        return res
    
    def eventualSafeNodes_v2(self, graph):
        # reverse graph for topo sort
        rev_graph = [[] for _ in range(len(graph))]
        safe = [False] * len(graph)
        q = []
        for st in range(len(graph)):
            if len(graph[st])==0:
                q.append(st)  # if is end node, it's safe
            for ed in graph[st]:
                rev_graph[ed].append(st)
        
        while len(q) > 0:
            j = q.pop(0)
            safe[j] = True
            for i in rev_graph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)
                    safe[i] = True
        return [i for i,v in enumerate(safe) if v]  
