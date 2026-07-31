/*
sort so that as we build the permuatations we naturally avoid duplicates

*/

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        visited.assign(nums.size(), false);
        sort(nums.begin(), nums.end());

        vector<int> curr;
        backtrack(nums, curr);

        return res;
    }

private:
    vector<vector<int>> res;
    vector<bool> visited;

    void backtrack(vector<int>& nums, vector<int>& curr) {
        if (curr.size() == nums.size()) {
            res.push_back(curr);
            return;
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])) {
                continue;
            }

            visited[i] = true;
            curr.push_back(nums[i]);
            backtrack(nums, curr);
            curr.pop_back();
            visited[i] = false;
        }
    }
};