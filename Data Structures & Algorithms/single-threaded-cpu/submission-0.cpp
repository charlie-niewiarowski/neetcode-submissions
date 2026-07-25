class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = tasks.size();

        vector<int> indices(n);
        iota(indices.begin(), indices.end(), 0);
        sort(indices.begin(), indices.end(), [&](int a, int b) {
            return tasks[a][0] < tasks[b][0] ||
                   (tasks[a][0] == tasks[b][0] && a < b);
        });

        auto cmp = [&](int a, int b) {
            if (tasks[a][1] == tasks[b][1]) return a > b;
            return tasks[a][1] > tasks[b][1];
        };
        priority_queue<int, vector<int>, decltype(cmp)> pq(cmp);
        
        int enq = 0, time = 0;
        vector<int> res;;
        while (!pq.empty() || enq < n) {
            while (enq < n && tasks[indices[enq]][0] <= time) {
                pq.push(indices[enq++]);
            }

            if (pq.empty()) {
                time = tasks[indices[enq]][0];
                continue;
            }

            int next = pq.top(); pq.pop();
            time += tasks[next][1];
            res.push_back(next);
        }

        return res;
    }
};