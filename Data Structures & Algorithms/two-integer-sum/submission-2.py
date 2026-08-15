class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for idx, num in enumerate(nums):
            if num in complement:
                return [complement[num], idx]
            complement[target - num] = idx