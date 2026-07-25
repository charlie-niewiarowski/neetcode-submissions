class Solution {
public:
    string reorganizeString(string s) {
        vector<int> freq(26, 0);
        for (const char& c : s) {
            freq[c - 'a'] += 1; 
        }

        priority_queue<pair<int, char>> max_heap;
        for (int i = 0; i < 26; ++i) {
            if (freq.at(i) > 0) {
                max_heap.push({freq[i], 'a' + i});
            }
        }

        string res = "";
        pair<int, char> prev = {0, ' '};

        while (!max_heap.empty() || prev.first > 0) {
            if (prev.first > 0 && max_heap.empty()) return "";

            auto [cnt, ch] = max_heap.top(); max_heap.pop();
            res += ch;
            cnt -= 1;

            if (prev.first > 0) {
                max_heap.push(prev);
                prev = {0, ' '};
            }
            if (cnt != 0) {
                prev = {cnt, ch};
            }
        }

        return res;
    }
};