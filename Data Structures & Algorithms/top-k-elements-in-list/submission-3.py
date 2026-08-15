class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {i : [] for i in range(1, len(nums) + 1)}
        res = []
        for n, f in Counter(nums).items():
            freq[f].append(n)
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res