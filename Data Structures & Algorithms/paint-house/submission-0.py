class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        ROWS, COLS = len(costs) + 1, 3
        dp = [[0] * COLS for i in range(ROWS)]

        for r in range(ROWS - 1):
            for c in range(COLS):
                dp[r + 1][c] = costs[r][c] + min(dp[r][(c + 1) % COLS], dp[r][(c - 1) % COLS])
        
        return min(dp[ROWS - 1])