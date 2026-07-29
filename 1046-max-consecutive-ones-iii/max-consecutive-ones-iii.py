class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        left = 0
        right = -1
        count_zeros = 0
        while (left < len(nums)):
            while (right + 1 < len(nums) and (nums[right + 1] == 1 or count_zeros < k)):
                right += 1
                if nums[right] == 0:
                    count_zeros += 1
            
            max_len = max(max_len, right - left + 1)
            if nums[left] == 0:
                count_zeros -= 1
                left += 1
            else:
                left += 1

        return max_len
