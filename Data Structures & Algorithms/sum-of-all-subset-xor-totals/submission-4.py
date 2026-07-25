class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        def backtrack(i, curr):
            if i == len(nums):
                self.res += curr
                return
        
            backtrack(i + 1, curr ^ nums[i])
            backtrack(i + 1, curr)
        
        backtrack(0, 0)
        return self.res