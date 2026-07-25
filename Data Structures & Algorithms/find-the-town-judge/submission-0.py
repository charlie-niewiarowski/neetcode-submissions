class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(list)
        outgoing = defaultdict(list)

        for u, v in trust:
            incoming[v].append(u)
            outgoing[u].append(v)
        
        res = []
        print(incoming, outgoing)
        for vertex in incoming:
            if len(incoming[vertex]) == n - 1 and vertex not in outgoing:
                res.append(vertex)

        return -1 if len(res) != 1 else res[0]