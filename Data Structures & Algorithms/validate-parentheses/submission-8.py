class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'{':'}','[':']','(':')'}
        stack = []
        for c in s:
            if c in parentheses:
                stack.append(c)
            elif stack:
                if parentheses[stack.pop()] != c:
                    return False
            else:
                return False
        return not stack
