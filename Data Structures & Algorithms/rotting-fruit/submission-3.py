class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        def addFruit(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1 or (r, c) in visited:
                return False
            q.append((r, c))
            visited.add((r, c))
            return True

        minutes = 0
        while q:
            added = False
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                
                for dr, dc in directions:
                    if addFruit(r + dr, c + dc):
                        added = True
                
            minutes += added
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return minutes

