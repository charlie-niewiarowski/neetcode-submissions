class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)

        for u, v in trust:
            delta[u] -= 1
            delta[v] += 1
        
        for vertex in delta:
            if delta[vertex] == n - 1:
                return vertex
        
        return -1