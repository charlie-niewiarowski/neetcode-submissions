/*
create 2D table
iterate backwards over the array and at each step:
    table[r][c] = is this a current word && is table[c][any] true?
*/


class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();

        vector<bool> can_break(n + 1);
        can_break[n] = true;

        for (int l = n - 1; l >= 0; --l) {
            for (int r = l; r < n; ++r) {
                if (matches_word(std::string_view(s).substr(l, r - l + 1), wordDict) && can_break[r + 1]) {
                    can_break[l] = true;
                    break;
                }
            }
        }

        return can_break[0];
    }
private:
    bool matches_word(const std::string_view& str, vector<string>& wordDict) {
        for (const auto& word : wordDict) {
            if (str == word) 
                return true;
        }

        return false;
    }
};
