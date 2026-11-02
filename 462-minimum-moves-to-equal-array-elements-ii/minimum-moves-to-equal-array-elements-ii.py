class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mediana = nums[len(nums) // 2]
        ans = 0
        for i in range(len(nums)):
            ans += abs(mediana - nums[i])

        return ans