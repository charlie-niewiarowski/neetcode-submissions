class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol, total = [], [], 0

        def backtrack(i):
            nonlocal total
            if i == n or total > target:
                if total == target and sol not in res:
                    res.append(sol[:])
                return

            backtrack(i + 1)

            total += nums[i]
            sol.append(nums[i])

            backtrack(i)

            sol.pop()
            total -= nums[i]

        backtrack(0)
        return res