class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        visited = set()

        def addCell(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or 
                (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            q.append((r, c))

        # initialize queue with treasures

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    addCell(r + dr, c + dc)
            dist += 1



