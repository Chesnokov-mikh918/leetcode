class Solution:
    def checkValidString(self, s: str) -> bool:
        low_balance = 0
        high_balance = 0
        for i in range(len(s)):
            if s[i] == '(':
                low_balance += 1
                high_balance += 1
            elif s[i] == ')':
                low_balance -= 1
                high_balance -= 1
            else:
                low_balance -= 1
                high_balance += 1

            if high_balance < 0:
                return False

            if low_balance < 0:
                low_balance = 0

        return low_balance == 0