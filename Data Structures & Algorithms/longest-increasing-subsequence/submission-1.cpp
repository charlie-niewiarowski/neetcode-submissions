class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> LIS(nums.size(), 1);

        for (unsigned int i = 0; i < nums.size(); ++i ) {
            int maxSub = 0;
            for (unsigned int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    maxSub = max(maxSub, LIS[j] + 1);
                }
            }
            LIS[i] = max(maxSub, LIS[i]);
        }

        int res = 0;
        for (const int& val : LIS) {
            res = max(res, val);
        }

        return res;
    }
};
