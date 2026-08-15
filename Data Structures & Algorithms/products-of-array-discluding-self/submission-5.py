class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = {}
        prev = 1
        for idx, num in enumerate(nums):
            products[idx] = prev
            prev = num * prev
        prev = 1
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(products[i] * prev)
            prev = nums[i] * prev
        return res[::-1]