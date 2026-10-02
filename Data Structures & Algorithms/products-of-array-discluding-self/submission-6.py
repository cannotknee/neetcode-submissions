class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMultiple = {}
        res = [0] * len(nums)
        prev = 1

        for i in range(len(nums)):
            leftMultiple[i] = prev
            prev = prev * nums[i]

        prev = 1

        for j in range(len(nums) - 1, -1, -1):
            res[j] = prev * leftMultiple[j]
            prev = prev * nums[j]

        return res