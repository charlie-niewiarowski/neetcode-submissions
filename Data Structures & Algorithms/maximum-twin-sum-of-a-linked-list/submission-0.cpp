/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int> vals;

        for (ListNode* curr{head}; curr != nullptr; curr = curr->next) {
            vals.push_back(curr->val);
        }

        int l{}, r{static_cast<int>(vals.size()) - 1}, res{};
        while (l < r) {
            res = max(res, vals[l++] + vals[r--]);
        }

        return res;
    }
};