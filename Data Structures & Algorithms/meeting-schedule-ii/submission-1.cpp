/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }

sort by ascending start times
iterate
    if there is a room that has an end time <= curr start time
        update that room's end time
    otherwise push a new room onto the heap
return heap.size() (or just increment and then return final value)

nlogn + n(logn + 1)
 */


class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b) {
            if (a.start == b.start) return a.end < b.end;
            return a.start < b.start;
        });

        std::priority_queue<int, vector<int>, std::greater<>> heap;
        for (const auto& interval : intervals) {
            if (!heap.empty() && heap.top() <= interval.start) {
                heap.pop();   
            }

            heap.push(interval.end);
        }

        return heap.size();
    }
};
