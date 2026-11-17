class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def sum_my(s: str):
            sum = 0
            for i in s:
                sum += int(i)

            return sum

        while len(s) > k:
            new_s = ""
            for i in range(0, len(s), k):
                new_s += str(sum_my(s[i:i + k]))

            s = new_s

        return s    