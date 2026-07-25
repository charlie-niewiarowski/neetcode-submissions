class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int l = 0, n = customers.size(), window_start = 0;
        int curr_diff = 0, max_diff = 0;
        for (int r = 0; r < n; ++r) {
            if (grumpy[r]) curr_diff += customers[r];
            if (r >= minutes) {
                if (grumpy[l]) curr_diff -= customers[l];
                ++l;
            }

            if (curr_diff > max_diff) {
                max_diff = curr_diff;
                window_start = l;
            }
        }

        int window_end = min(window_start + minutes - 1, n - 1);
        int res = 0;
        for (int i = 0; i < n; ++i) {
            if (!grumpy[i] || (i >= window_start && i <= window_end)) res += customers[i];
        }

        return res;
    }
};