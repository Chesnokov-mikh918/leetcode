class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_len = 0
        len_arrays = {0: -1}
        for i, num in enumerate(nums):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            if prefix_sum in len_arrays:
                max_len = max(max_len, i - len_arrays[prefix_sum])
            else:
                len_arrays[prefix_sum] = i
        return max_len