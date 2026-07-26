class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        right = 0
        left = 0
        max_len = 0
        while (left < len(nums)):
            if (nums[left] % 2 != 0 or nums[left] > threshold):
                left += 1
                continue
            right = left

            while (right + 1 < len(nums)):
                if ((nums[right] % 2 == nums[right + 1] % 2) or nums[right + 1] > threshold):
                    break
                right += 1

            max_len = max(max_len, right - left + 1)
            left = right + 1  

        return max_len