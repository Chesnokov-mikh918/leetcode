class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        count_dict = dict()
        res_sum = 0
        ans_list = []
        for i in range(0, k):
            count_dict[nums[i]] = count_dict.get(nums[i], 0) + 1
        
        for element in sorted(count_dict.keys(), key = lambda val: [count_dict[val], val], reverse=True)[:x]:
            res_sum += count_dict[element] * element
        ans_list.append(res_sum)

        for i in range(k, len(nums)):
            count_dict[nums[i]] = count_dict.get(nums[i], 0) + 1
            count_dict[nums[i - k]] = count_dict.get(nums[i - k], 0) - 1
            res_sum = 0
            for element in sorted(count_dict.keys(), key = lambda val: [count_dict[val], val], reverse=True)[:x]:
                res_sum += count_dict[element] * element
            ans_list.append(res_sum)
        return ans_list