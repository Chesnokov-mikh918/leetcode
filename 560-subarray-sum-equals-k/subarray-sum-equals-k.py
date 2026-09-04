class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_pref = {0: 1}
        count = 0
        prefix_cur = 0
        for i in range(len(nums)):
            prefix_cur += nums[i]
            if prefix_cur - k in count_pref:
                count += count_pref[prefix_cur - k]
            count_pref[prefix_cur] = count_pref.get(prefix_cur, 0) + 1
        return count