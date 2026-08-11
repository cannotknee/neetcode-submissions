class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        numSet = set(nums)
        greatest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                curr = 1
                while num + curr in numSet:
                    curr += 1
                greatest = max(greatest, curr)
        return greatest