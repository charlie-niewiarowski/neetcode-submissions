class Solution {
public:
    string longestPalindrome(string s) {
        int resIdx = 0, resLen = 0;
        int n = s.size();

        vector<vector<bool>> dp(n, vector<bool>(n, false));

        for (int i{n - 1}; i >= 0; --i) {
            for (int j{i}; j < n; ++j) {
                if (s[i] == s[j] && (j - i <= 2 || dp[i + 1][j - 1])) {
                    dp[i][j] = true;
                    if (j - i + 1 > resLen) {
                        resIdx = i;
                        resLen = j - i + 1;
                    }
                }
            }
        }

        return string(s.begin() + resIdx, s.begin() + resIdx + resLen);
    }
};
