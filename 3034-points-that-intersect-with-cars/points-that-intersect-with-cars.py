class Solution:
    def is_overlapping(self, nums1: List[int], nums2: List[int]) -> bool:
        return max(nums1[0], nums2[0]) <= min(nums1[1], nums2[1])

    def merge_two(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [min(nums1[0], nums2[0]), max(nums1[1], nums2[1])]

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res = []
        nums.sort(key=lambda val: val[0])
        cur = nums[0]
        for i in range(1, len(nums)):
            if self.is_overlapping(nums[i], cur):
                cur = self.merge_two(nums[i], cur)
            else:
                res.append(cur)
                cur = nums[i]
        res.append(cur)
        count = 0
        for i in res:
            count += (i[1] - i[0] + 1)
        return count