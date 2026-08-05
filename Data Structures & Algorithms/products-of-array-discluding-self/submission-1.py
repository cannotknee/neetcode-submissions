from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = defaultdict()
        prev = None
        res = [0] * len(nums)

        for i in range(len(nums)):
            if prev == None:
                products[i] = nums[i]
            else:
                products[i] = nums[i] * prev
            prev = products[i]

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                res[j] = products[j - 1]
                prev = nums[j]
            elif j > 0:
                res[j] = products[j - 1] * prev
                prev *= nums[j]
            elif j == 0:
                res[j] = prev
                
        return res