class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # верно и для отрицательных и для положительных
        min_mean = min(nums)
        max_mean = max(nums)
        ans = 0

        # верно и для отрицательных и для положительных
        for i in range(len(nums)):
            ans += (nums[i] - min_mean)

        return ans       
            