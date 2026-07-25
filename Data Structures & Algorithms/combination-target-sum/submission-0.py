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
            
            # move on to the next 
            backtrack(i + 1)

            num = nums[i]
            # use value
            sol.append(num)
            total += num

            # we can stay on this num
            backtrack(i)

            # we can not use the num
            backtrack(i + 1)

            sol.pop()
            total -= num

        backtrack(0)
        return res

