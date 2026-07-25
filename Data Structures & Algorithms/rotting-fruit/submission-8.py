class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        minutes, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        def addFruit(r, c):
            nonlocal fresh
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r, c))
            fresh -= 1


        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    addFruit(r + dr, c + dc)
            minutes += 1
        

        return minutes if fresh == 0 else -1

