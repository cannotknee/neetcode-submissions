class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for idx, num in enumerate(nums):
            left = idx + 1
            right = len(nums) - 1
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            while left < right:
                total = num + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res