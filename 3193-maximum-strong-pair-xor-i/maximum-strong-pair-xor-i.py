class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0
        nums.sort()
        i = 0
        for j in range(0, len(nums)):
            while (nums[j] > 2*nums[i]):
                i += 1
            for k in range(i, j + 1):
                max_xor = max(max_xor, nums[k] ^ nums[j])
        return max_xor


