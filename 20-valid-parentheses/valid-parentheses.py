class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brack = {'[': ']', '(': ')', '{': '}'}
        for i in range(len(s)):
            if s[i] in open_brack:
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                last_char = stack.pop()
                if open_brack[last_char] != s[i]:
                    return False
        return len(stack) == 0