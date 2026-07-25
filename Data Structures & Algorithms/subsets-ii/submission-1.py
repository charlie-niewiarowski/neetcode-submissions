class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, sol):
            if i == len(nums):
                if sorted(sol[:]) not in res:
                    res.append(sorted(sol[:]))
                return
            
            sol.append(nums[i])
            backtrack(i + 1, sol)
            sol.pop()

            backtrack(i + 1, sol)
        
        backtrack(0, sol)
        return res