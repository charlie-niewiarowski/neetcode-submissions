class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count, max_count = 0, 0
        s = set(nums)

        for n in nums:
            if (n - 1) not in s:
                count = 0
                while n in s:
                    count += 1
                    n += 1
                max_count = max(count, max_count)
        return max_count
