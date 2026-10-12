class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # подготовка массива количества единиц в каждом разряде
        count = [0] * 40
        for num in nums:
            for j in range(40):
                count[j] += (num >> j) & 1
        # создаем максимальные числа
        max_sum = 0
        for i in range(k):
            res_i = 0
            for j in range(40):
                if count[j] != 0:
                    res_i += 1 << j
                    count[j] -= 1
                else:
                    res_i = res_i << 0

            max_sum += res_i**2

        return max_sum % (10**9 + 7)
                

