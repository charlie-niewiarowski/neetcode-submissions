class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
                if zero_count >= 2:
                    return [0] * len(nums)
            else:
                product *= n
        
        print(product)
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(product)
            elif zero_count > 0 :
                res.append(0)
            else:
                res.append(product // nums[i])
        
        return res