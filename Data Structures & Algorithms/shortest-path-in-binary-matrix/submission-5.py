class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return 1
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        target = (ROWS - 1, COLS - 1)

        visit = set((0, 0))
        q = deque([(0, 0)])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

        steps = 1
        while q:
            steps += 1
            for i in range(len(q)):
                r, c = q.popleft()   

                for dr, dc in directions:
                    child = (r + dr, c + dc)
                    if (r + dr < 0 or r + dr >= ROWS or 
                    c + dc < 0 or c + dc >= COLS or 
                    child in visit or grid[r + dr][c + dc] == 1):
                        continue

                    if child == target:
                        return steps
                    
                    q.append(child)
                    visit.add(child)
        return -1




