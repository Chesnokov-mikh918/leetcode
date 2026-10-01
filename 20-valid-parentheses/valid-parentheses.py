class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for i in range(len(s)):
            if s[i] in brackets.values():
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                last_brack = stack.pop()
                if brackets[s[i]] != last_brack:
                    return False
        return len(stack) == 0