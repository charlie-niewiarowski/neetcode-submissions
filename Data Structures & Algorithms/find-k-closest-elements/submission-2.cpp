/*
iterate over a sliding window
compare l&r ptrs' distances from x to previous best
return the slice of the ptrs
*/

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int curr{
            std::accumulate(
                arr.begin(), 
                arr.begin() + k, 
                0, 
                [=](int sum, int value) {
                    return sum + std::abs(value - x);
                }
            )
        };

        int best_val{curr}, best_left{};
        for (int left{1}; left + k <= static_cast<int>(arr.size()); ++left) {
            curr -= std::abs(arr[left - 1] - x);
            curr += std::abs(arr[left + k - 1] - x);

            if (curr < best_val) {
                best_val = curr;
                best_left = left;
            }
        }

        return {
            arr.begin() + best_left,
            arr.begin() + best_left + k
        };
    }
};