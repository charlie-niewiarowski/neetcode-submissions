class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        return max(helper(vector<int>(nums.begin(), nums.end() - 1)), helper(vector<int>(nums.begin() + 1, nums.end())));
    }

    int helper(vector<int> nums) {
        int n = nums.size();
        if (n == 1) return nums[0];

        vector<int> dp(n + 1, 0);
        dp[n - 1] = nums[n - 1];

        for (int i = n - 2; i >= 0; --i) {
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1]);
        }

        return dp[0];
    }
};
