class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1

            for i in range(n):
                if visit[i]:
                    continue
                
                currDist = (abs(points[node][0] - points[i][0]) + 
                            abs(points[node][1] - points[i][1]))
                dist[i] = min(dist[i], currDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            edges += 1
            node = nextNode
        
        return res
