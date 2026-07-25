class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = grid[0][0]

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) == (0, 0):
                    continue

                left = dp[r][c - 1] if c > 0 else float('inf')
                up = dp[r - 1][c] if r > 0 else float('inf')
                dp[r][c] = grid[r][c] + min(left, up)
        
        return dp[ROWS - 1][COLS - 1]