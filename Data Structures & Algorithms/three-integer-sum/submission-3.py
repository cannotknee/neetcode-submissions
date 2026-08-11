class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()
        for idx, num in enumerate(nums):
            if nums[idx] == nums[idx - 1] and idx > 0:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -num:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[right] + nums[left] < -num:
                    left += 1
                else:
                    right -= 1
        return res
# what: 3 digits where the sum == 0
# what DS: 2 pointers
# condition: indices must be distinct (no duplicate), i = - (j + k)
# brute force: loop through for every digit

# -4, -1, -1, 0, 1, 2