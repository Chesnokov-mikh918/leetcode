class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = dict()
        left = 0
        right = -1
        max_len = 0 
        while left < len(nums) and right < len(nums):
            while right + 1 < len(nums) and freq.get(nums[right + 1], 0) < k: 
                freq[nums[right + 1]] = freq.get(nums[right + 1], 0) + 1
                right += 1
            max_len = max(max_len, right - left + 1) # мб не + 1
            if right + 1 < len(nums):
                freq[nums[left]] -= 1
                left += 1
            else:
                break 
        return max_len

             