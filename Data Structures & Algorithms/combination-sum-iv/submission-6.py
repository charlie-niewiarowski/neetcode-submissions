class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1

        dp = [0] * (target + 1)
        for goal in range(1, target + 1):
            for n in nums:
                if goal - n > 0:
                    dp[goal] += dp[goal - n]
                elif goal - n == 0:
                    dp[goal] += 1
        
        return dp[target]
                