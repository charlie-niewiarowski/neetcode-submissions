/**
There are two "types" of subarray sums. 
The first is the subarray sum within the middle of the array (it does not wrap around)
The second is the subarray sum that wraps about the array

For either "type" of subarray sum, whatever we have left is the minimum subarray sum of the other type.
For example, if we take the maximum subarray sum of nums, and this subarray does not wrap around, then what's left
is not only the minimum subarray sum of nums, but it also wraps around.
So, if we keep track of the minimum subarray sum of nums that doesn't wrap around, what we don't have left is the maximum
subarray sum of nums that does wrap around.

Thus we can keep track of the maximum and minimum subarray sums assuming that nums is not circular. Then, we can use the minimum subarray
sum to derive the maximum subarray sum that uses the circular nature of nums, and take the maximum of that and the non-circular maximum subarray sum.
**/

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int max_sum = nums[0], min_sum = nums[0];

        int curr_max = 0, curr_min = 0, sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            curr_max += nums[i]; curr_min += nums[i]; sum += nums[i];
            max_sum = max(max_sum, curr_max);
            min_sum = min(min_sum, curr_min);

            if (curr_max < 0) curr_max = 0;
            if (curr_min > 0) curr_min = 0;
        }

        if (min_sum == sum) return max_sum;
        return max(max_sum, sum - min_sum);
    }
};