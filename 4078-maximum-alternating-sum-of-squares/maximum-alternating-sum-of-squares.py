class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda val: abs(val))
        score = 0
        for el in nums[len(nums) // 2:]:
            score += el**2
        
        for el in nums[:len(nums) // 2]:
            score -= el**2

        return score