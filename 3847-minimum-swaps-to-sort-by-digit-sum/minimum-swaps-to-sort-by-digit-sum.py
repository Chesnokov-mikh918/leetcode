class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_sum_nums(num):
            s = str(num)
            sum_i = 0
            for i in s:
                sum_i += int(i)
            return sum_i

        in_pos = dict()
        for i in range(len(nums)):
            in_pos[nums[i]] = i

        nums.sort(key=lambda val: (get_sum_nums(val), val))

        cycles = 0
        seen = [False] * len(nums)
        for i in range(len(nums)):
            if not seen[i]:
                cycles += 1
                j = i
                while not seen[j]:
                    seen[j] = True
                    j = in_pos[nums[j]]

        return len(nums) - cycles
