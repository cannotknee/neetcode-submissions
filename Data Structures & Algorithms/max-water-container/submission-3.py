class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water = 0
        while left < right:
            if heights[left] >= heights[right]:
                area = heights[right] * (right - left)
                right -= 1
            elif heights[right] >= heights[left]:
                area = heights[left] * (right - left)
                left += 1
            water = max(water, area)
        return water
