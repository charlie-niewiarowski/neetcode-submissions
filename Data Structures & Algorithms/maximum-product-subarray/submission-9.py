class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin = currMax = 1
                continue
            
            tmp = currMax * n
            currMax = max(n * currMax, n * currMin)
            currMin = min(tmp, currMin * n, n)
             
            res = max(res, currMax)
        
        return res