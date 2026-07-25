class Solution {
private:
    vector<vector<int>> heights;
    int rows, cols;

    vector<pair<int, int>> directions{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    void dfs(int r, int c, vector<vector<bool>>&ocean) {
        ocean[r][c] = true;

        for (const auto [dr, dc] : directions) {
            int nr = r + dr, nc = c + dc;
            if (!out_of_bounds(nr, nc) && !ocean[nr][nc] && heights[r][c] <= heights[nr][nc]) {
                dfs(nr, nc, ocean);
            }
        }
    }

    bool out_of_bounds(int r, int c) { return r < 0 || c < 0 || r >= rows || c >= cols; }
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        this->heights = heights;
        rows = heights.size();
        cols = heights[0].size();

        vector<vector<bool>> pacific(rows, vector<bool>(cols, false));
        vector<vector<bool>> atlantic(rows, vector<bool>(cols, false));

        for (int r = 0; r < rows; ++r) {
            dfs(r, 0, pacific);
            dfs(r, cols - 1, atlantic);
        }
        for (int c = 0; c < cols; ++c) {
            dfs(0, c, pacific);
            dfs(rows - 1, c, atlantic);
        }

        vector<vector<int>> res;
        for (int r = 0; r < rows; ++r) { 
            for (int c = 0; c < cols; ++c) {
                if (pacific[r][c] && atlantic[r][c]) res.push_back({r, c});
            }
        }

        return res;
    }
};
