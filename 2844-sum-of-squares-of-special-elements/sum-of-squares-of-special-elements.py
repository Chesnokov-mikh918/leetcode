class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum_i = 0
        n = len(nums)
        for i in range(n):
            if n % (i + 1) == 0:
                sum_i += nums[i]*nums[i]
        return sum_i