class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water = 0
        while left < right:
            if heights[left] >= heights[right]:
                water = max(water, heights[right] * (right - left))
                right -= 1
            elif heights[right] >= heights[left]:
                water = max(water, heights[left] * (right - left))
                left += 1
        return water
