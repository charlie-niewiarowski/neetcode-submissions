# res = largest value in array
# for each value in the array, flip the ith bit

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n
        for i in range(n):
            xor ^= i ^ nums[i]
        return xor