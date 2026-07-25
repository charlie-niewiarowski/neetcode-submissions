class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        N = len(edges)
        
        pars = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            if pars[n1] == n1:
                return n1
            pars[n1] = find(pars[n1])
            return pars[n1]   
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                pars[p2] = p1
                rank[p1] += rank[p2]
            else:
                pars[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        res = n
        for n1, n2 in edges:
            if union(n1, n2):
                res -= 1
        return res
            
