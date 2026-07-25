/*
loop over K
at each iteration:
    update heap
    pop the max-profit project
    add the profit to your curr capital

update heap
    use a min heap to pop all indices where capital[i] < curr capiutal
    push those onto the primary max heap
*/

class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        auto profit_cmp = [&](int a, int b) {
            return profits[a] < profits[b];
        };

        auto capital_cmp = [&](int a, int b) {
            return capital[a] > capital[b];
        };

        std::priority_queue<int, vector<int>, decltype(profit_cmp)>
            profit_heap{profit_cmp};

        std::priority_queue<int, vector<int>, decltype(capital_cmp)>
            capital_heap{capital_cmp};

        size_t n{capital.size()};
        for (size_t i{}; i < n; ++i) {
            capital_heap.push(i);
        }

        for (int i{}; i < k; ++i) {
            int idx{capital_heap.top()};
            while (!capital_heap.empty() && capital[idx] <= w) {
                capital_heap.pop();
                profit_heap.push(idx);
                idx = capital_heap.top();
            }

            if (!profit_heap.empty()) {
                w += profits[profit_heap.top()];
                profit_heap.pop();
            }
        }

        return w;
    }
};