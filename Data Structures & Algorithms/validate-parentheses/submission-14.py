class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in bracket_dict.keys():
                stack.append(char)
            else:
                if stack:
                    current_top = stack.pop()
                    if char == bracket_dict[current_top]:
                        continue
                return False
        
        return not stack