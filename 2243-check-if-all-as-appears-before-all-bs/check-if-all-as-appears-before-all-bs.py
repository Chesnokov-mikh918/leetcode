class Solution:
    def checkString(self, s: str) -> bool:
        last_a = -1
        first_b = -1
        flag = True

        for i in range(len(s)):
            if s[i] == 'a':
                last_a = i
            if s[i] == 'b' and flag:
                first_b = i
                flag = False

        if first_b == -1 or last_a == -1:
            return True

        return last_a < first_b