class Solution:
    def get_number(self, nums: List[int]) -> int:
        current_value = 0
        for i in range(32):
            if (nums[i] > 0):
                current_value |= (1 << i) 
        return current_value

    def set_bits(self, nums: List[int], need_set_numb) -> None:
        for i in range(32):
            if need_set_numb & (1 << i):  
                nums[i] += 1

    def remove_bits(self, nums: List[int], need_remove_numb) -> None:
        for i in range(32):
            if need_remove_numb & (1 << i):
                nums[i] -= 1

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if (k == 0):
            return 1
        left = 0
        right = 0
        min_len = 10**10
        bits = [0 for _ in range(32)]
        self.set_bits(bits, nums[0])
        while (left < len(nums)):
            while (right + 1 < len(nums) and self.get_number(bits) < k):
                self.set_bits(bits, nums[right + 1])
                right += 1

            if (self.get_number(bits) >= k):
                min_len = min(min_len, right - left + 1)

            self.remove_bits(bits, nums[left])
            left += 1
        return min_len if min_len != 10**10 else -1