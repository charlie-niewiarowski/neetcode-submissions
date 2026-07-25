class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort()
        for u, v in tickets:
            adj[u].append(v)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            elif src not in adj:
                return False
            
            tmp = list(adj[src])
            for i, v in enumerate(tmp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v): return True

                res.pop()
                adj[src].insert(i, v)
            return False

        dfs("JFK")
        return res