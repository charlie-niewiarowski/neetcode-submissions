class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            one, two = 0, 0
            for num in nums:
                newTwo = max(two, num + one)
                one = two
                two = newTwo
            return two
        
        return max(nums[0], dp(nums[1:]), dp(nums[:-1]))