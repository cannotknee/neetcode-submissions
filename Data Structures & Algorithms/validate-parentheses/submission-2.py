class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parent = {'[': ']', '{': '}', '(': ')'}

        for i in s:
            if i in parent.keys():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                opening = stack.pop()
                if i != parent[opening]:
                    return False
        return not stack