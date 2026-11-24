from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # инициализация всего
        max_len = 0

        # брут форс решение
        for i in range(len(nums)):
            cur_len = 1
            prod = nums[i]
            gcd_cur = nums[i]
            lcm_cur = nums[i]
            for j in range(i + 1, len(nums)):
                prod *= nums[j]
                gcd_cur = gcd(gcd_cur, nums[j])
                lcm_cur = lcm(lcm_cur, nums[j])
                cur_len += 1

                if prod == lcm_cur * gcd_cur:
                    max_len = max(max_len, cur_len)

        return max_len