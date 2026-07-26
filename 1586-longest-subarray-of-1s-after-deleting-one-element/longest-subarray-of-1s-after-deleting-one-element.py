class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = -1
        count_zero = 0
        max_len = 0
        while (left < len(nums)):
            while (right + 1 < len(nums)):
                if (nums[right + 1] == 0 and count_zero == 1):
                    break
                if (nums[right + 1] == 0):
                    count_zero += 1
                right += 1
            max_len = max(max_len, right - left) # return here
            if (nums[left] == 0):
                count_zero -= 1
            left += 1
        return max_len