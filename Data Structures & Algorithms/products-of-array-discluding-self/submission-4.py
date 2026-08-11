from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cumProduct = {}
        prev = 1
        res = []
        for i in range(0, len(nums)):
            if i == 0:
                cumProduct[i] = 1
            else:
                cumProduct[i] = nums[i - 1] * prev 
                prev = cumProduct[i]
        right = 1
        for j in range(len(nums) - 1, -1, -1):
            res.append(cumProduct[j] * right)
            right = nums[j] * right
        return res[::-1]