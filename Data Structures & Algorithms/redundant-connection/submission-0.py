class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # BFS
        # Go node by node, adding each of the node's children and adding them to a set
        # If a node is already in the set we store the index of the current edge as the one to remove
        n = len(edges)
        disjoint = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(n):
            if n == disjoint[n]:
                return disjoint[n]
            disjoint[n] = find(disjoint[n])
            return disjoint[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                disjoint[p2] = p1
                rank[p1] += rank[p2]
            else:
                disjoint[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]