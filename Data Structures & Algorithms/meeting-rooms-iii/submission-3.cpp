/*
heap for most times
we need to keep of:
    the next meeting (lowest start time)
    next room (lowest ready time)

heapify the meetings vector as a PQ
pop from meetings heap, pop from room time heap, add together, push to room time heap, increment room's # of meetings
extract max

*/

class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        priority_queue<int, vector<int>, greater<int>> available;

        priority_queue<
            pair<long long, int>,
            vector<pair<long long, int>>,
            greater<pair<long long, int>>
        > busy;

        for (int room = 0; room < n; ++room)
            available.push(room);

        sort(meetings.begin(), meetings.end());

        std::vector<int> room_bookings(n, 0);
        for (auto& meeting : meetings) {
            int start{meeting[0]}, end{meeting[1]};

            while (!busy.empty() && busy.top().first <= start) {
                available.push(busy.top().second);
                busy.pop();
            }

            if (!available.empty()) {
                int room = available.top();
                available.pop();

                busy.push({end, room});
                room_bookings[room]++;
            }
            else {
                auto [finish, room] = busy.top();
                busy.pop();

                busy.push({finish + end - start, room});
                room_bookings[room]++;
            }
        }

        int best_idx{}, best_val{};
        for (int i{}; i < n; ++i) {
            if (room_bookings[i] > best_val) {
                best_val = room_bookings[i];
                best_idx = i;
            }
        }

        return best_idx;
    }
};