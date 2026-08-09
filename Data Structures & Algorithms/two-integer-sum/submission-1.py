class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in remainder:
                return [remainder[complement], idx]
            remainder[num] = idx
        
        # track indices where they sum to the target
        # store remainders for lookup
        # dictionary
        # only 1 pair and it always exists