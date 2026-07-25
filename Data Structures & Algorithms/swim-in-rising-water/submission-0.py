class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def canReach(m):
            nonlocal ROWS, COLS
            q = deque([(0, 0)])
            visited = set()

            while q:
                r, c = q.popleft()
                visited.add((r, c))

                if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] > m:
                    continue
                elif (r, c) == (ROWS - 1, COLS - 1):
                    return True
                
                for dr, dc in dirs:
                    if (r + dr, c + dc) not in visited:
                        q.append((r + dr, c + dc))
            
            return False

        maxVal = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxVal = max(maxVal, grid[r][c])

        l, r = grid[ROWS - 1][COLS - 1], maxVal
        res = 0
        while l <= r:
            m = (l + r) // 2
            
            if canReach(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
            