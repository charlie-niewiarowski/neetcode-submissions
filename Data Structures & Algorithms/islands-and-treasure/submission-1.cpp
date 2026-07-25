class Solution {
private:
    int INF = 2147483647;
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        vector<pair<int, int>> directions{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        deque<pair<int,int>> q;
        for (int r = 0; r < rows; ++r)
            for (int c = 0; c < cols; ++c)
                if (grid[r][c] == 0)
                    q.push_back({r, c});

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop_front();


            for (auto [dr, dc] : directions) {
                int nr = r + dr, nc = c + dc;
                if (nr >= 0 && nc >= 0 && nr < rows && nc < cols && grid[nr][nc] == INF) {
                    q.push_back({nr, nc});
                    grid[nr][nc] = grid[r][c] + 1;
                }
            }
            
        }
    }
};
