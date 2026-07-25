class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int n = costs.size();
        vector<vector<int>> dp(n, vector<int>(3, 0));

        for (int i = 0; i < 3; ++i) {
            dp[n - 1][i] = costs[n - 1][i];
        }

        for (int r = n - 2; r >= 0; --r) {
            for (int c = 0; c < 3; ++c) {
                dp[r][c] = costs[r][c] + min(dp[r + 1][(c + 1) % 3], dp[r + 1][(c + 2) % 3]);
            }
        }

        return min(min(dp[0][0], dp[0][1]), dp[0][2]);
    }
};