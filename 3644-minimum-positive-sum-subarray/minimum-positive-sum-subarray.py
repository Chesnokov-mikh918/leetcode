class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = 10**10
        for i in range(l, r + 1):
            sum_j = 0
            for j in range(0, i):
                sum_j += nums[j]
            
            if (sum_j > 0):
                ans = min(ans, sum_j)
            
            for k in range(i, len(nums)):
                sum_j += nums[k]
                sum_j -= nums[k - i]
                if (sum_j > 0):
                    ans = min(ans, sum_j)
                    
        if (ans == 10**10):
            return -1
        return ans

