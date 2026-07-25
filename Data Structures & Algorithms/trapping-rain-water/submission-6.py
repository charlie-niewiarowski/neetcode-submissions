class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] 
        water = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom_h = height[stack.pop()]

                if not stack:
                    break
                
                left_idx = stack[-1]
                width = i - left_idx - 1
                depth = min(height[left_idx], h) - bottom_h
                water += depth * width

            stack.append(i)

        return water
            


                