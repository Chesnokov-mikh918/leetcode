class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                s_part = ""
                while stack[-1] != '(':
                    s_part += stack.pop()[::-1]
                stack.pop()
                stack.append(s_part)
            else:
                stack.append(s[i])
        return "".join(stack)