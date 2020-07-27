import pdb

class Solution:
    def findItinerary(self, tickets):
        """ input| tickets: List[List[str]]
           output| List[str] """
        # construct graph
        num = len(tickets)
        node_dict = {}
        for s, t in tickets:
            if s not in node_dict:
                node_dict[s] = [t]
            else:
                node_dict[s].append(t)
        for key in node_dict:
            node_dict[key].sort()
        # search and update graph
        res = ['JFK']  # init with start station
        out = []
        def dfs(res, used=0):
            nonlocal out
            # terminate condition
            if used == num:
                out.append(res.copy())
                return True
            cur_node = res[-1]
            if cur_node in node_dict:
                for _ in range(len(node_dict[cur_node])):
                    next_node = node_dict[cur_node].pop(0)
                    res.append(next_node)
                    if dfs(res, used+1):
                        return True  # prun!
                    res.pop()
                    node_dict[cur_node].append(next_node)
            return False

        dfs(res, 0)
        return out[0]


if __name__=='__main__':
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    sol = Solution()
    res = sol.findItinerary(tickets)
    print(res)
