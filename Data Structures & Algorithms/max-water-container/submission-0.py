class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        left = 0
        right = length - 1
        result = 0
        
        while left < right:
            if heights[left] >= heights[right]:
                area = heights[right] * (right - left)
                right -= 1
            elif heights[right] >= heights[left]:
                area = heights[left] * (right - left)
                left += 1
            result = max(result, area)
        
        return result