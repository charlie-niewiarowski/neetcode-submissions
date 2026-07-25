class Solution:
    class UFS:
        def __init__(self, n):
            self.pars = [i for i in range(n)]
            self.rank = [1] * n

        def find(self, n):
            if self.pars[n] == n:
                return n
            self.pars[n] = self.find(self.pars[n])
            return self.pars[n]
        
        def union(self, n1, n2):
            p1, p2 = self.find(n1), self.find(n2)
            if p1 == p2:
                return False
            
            if self.rank[p1] > self.rank[p2]:
                self.pars[p2] = p1
                self.rank[p1] += self.rank[p2]
            else:
                self.pars[p1] = p2
                self.rank[p2] += self.rank[p1]
            return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        N = len(edges)
        if N != n - 1:
            return False

        ufs = self.UFS(n)
        for u, v in edges:
            if not ufs.union(u, v):
                return False
        
        
        for i in range(1, n):
            if ufs.pars[i - 1] != ufs.pars[i]:
                return False
        
        return True