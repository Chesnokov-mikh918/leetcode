class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        s = ""
        
        if num * 9 < sum:
            return s

        cur_sum = 0
        while len(s) < num and cur_sum + 9 < sum:
            s += '9'
            cur_sum += 9
        
        if len(s) < num:
            s += str(sum - cur_sum)

        while len(s) < num:
            s += '0'

        return s