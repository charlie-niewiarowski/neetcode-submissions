class Solution {
public:
    int climbStairs(int n) {
        int one_above = 1, two_above = 1;

        for (int i{n - 2}; i >= 0; --i) {
            int temp = one_above + two_above;
            two_above = one_above;
            one_above = temp;
        }

        return one_above;
    }
};
