class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > middle:
                right = middle
            else:
                left = middle + 1
        return left
