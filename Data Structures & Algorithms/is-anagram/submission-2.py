from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = Counter()
        for char in s:
            seen[char] += 1
        for char in t:
            if seen[char] == 0:
                return False
            seen[char] -= 1
        return True
    # need to check same chars in both strs
    # can have duplicates
    # Counter() will help