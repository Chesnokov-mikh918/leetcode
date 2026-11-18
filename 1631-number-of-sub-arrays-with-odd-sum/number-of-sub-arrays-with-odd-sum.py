class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # пустой подмассив четный
        even = 1
        odd = 0
        parity = 0 # parity это четность
        ans = 0

        # префиксный массив четности по сути, надо чтоб разница преф сумм была из четн и нечетн слагаемых или наоборот, тогда разность нечетная
        for i in range(len(arr)):
            parity = (parity + arr[i]) % 2
            if parity == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % (10 ** 9 + 7)
