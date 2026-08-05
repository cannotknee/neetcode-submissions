class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmapS = {}
        hashmapT = {}
        for i in range(len(s)):
            if s[i] in hashmapS:
                hashmapS[s[i]] += 1
            else:
                hashmapS[s[i]] = 1
            if t[i] in hashmapT:
                hashmapT[t[i]] += 1
            else:
                hashmapT[t[i]] = 1
        for key, value in hashmapS.items():
            if key not in hashmapT:
                return False
            if hashmapS[key] != hashmapT[key]:
                return False
        return True