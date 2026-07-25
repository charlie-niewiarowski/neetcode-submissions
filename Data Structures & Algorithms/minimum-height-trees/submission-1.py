

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        edge_counts = {}
        leaves = deque()

        for src, neighbors in adj.items():
            edge_counts[src] = len(neighbors)
            if len(neighbors) == 1:
                leaves.append(src)
        
        while leaves:
            if n <= 2:
                return list(leaves)

            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1

                for nei in adj[node]:
                    edge_counts[nei] -= 1
                    if edge_counts[nei] == 1:
                        leaves.append(nei)