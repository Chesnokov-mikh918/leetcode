class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in range(len(tokens)):
            if tokens[i] not in '*/+-':
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == '+':
                    stack.append(a + b)
                if tokens[i] == '-':
                    stack.append(a - b)
                if tokens[i] == '*':
                    stack.append(a * b)
                if tokens[i] == '/':
                    stack.append(int(a / b))
        return stack[-1]