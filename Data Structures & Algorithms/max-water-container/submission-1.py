class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while (l < r):
            area = min(heights[r], heights[l]) * (r - l)
            max_area = max(max_area, area)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return max_area