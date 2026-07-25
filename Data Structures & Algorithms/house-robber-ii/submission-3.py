class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        a = [0] * (n - 1)
        b = [0] * (n - 1)
        a[0], a[1] = nums[0], max(nums[0], nums[1])
        b[0], b[1] = nums[n - 1], max(nums[n - 1], nums[n - 2])

        for i in range(2, n - 1):
            a[i] = max(a[i - 1], nums[i] + a[i - 2])
            b[i] = max(b[i - 1], nums[n - i - 1] + b[i - 2])

        return max(a[-1], b[-1])