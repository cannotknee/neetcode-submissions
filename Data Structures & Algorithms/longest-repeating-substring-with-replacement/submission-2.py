class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        left = 0
        seen = {}
        res = 0
        maxf = 0
        for right, char in enumerate(s):
            seen[char] = seen.get(char, 0) + 1
            maxf = max(maxf, seen[char])
            while (right - left + 1) - maxf > k:
                seen[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
                
# replace up to k times
# sliding window to track longest substring
# how to identify