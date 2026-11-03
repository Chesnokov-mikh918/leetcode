class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_el = max(nums)
        ans = 0

        for i in range(len(nums)):
            ans += max_el - nums[i]

        return ans