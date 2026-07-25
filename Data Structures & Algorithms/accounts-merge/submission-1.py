class DSU:
    def __init__(self, n):
        self.pars = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        if self.pars[n] != n:
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

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        forest = DSU(len(accounts))
        emailToName = {} # Email -> index in the forest

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToName:
                    forest.union(i, emailToName[e])
                else:
                    emailToName[e] = i
        
        emailGroup = defaultdict(list)
        for e, i in emailToName.items():
            rep = forest.find(i)
            emailGroup[rep].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res



