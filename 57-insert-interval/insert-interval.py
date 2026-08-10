class Solution:
    def is_overlapping(self, nums1: List[int], nums2: List[int]) -> bool:
        return max(nums1[0], nums2[0]) <= min(nums1[1], nums2[1])

    def merge_two(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [min(nums1[0], nums2[0]), max(nums1[1], nums2[1])]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_array = []
        merging = False
        if len(intervals) == 0:
            return [newInterval]
        for i in range(len(intervals)):
            if self.is_overlapping(intervals[i], newInterval):
                newInterval = self.merge_two(intervals[i], newInterval)
            else:
                if not merging and newInterval[1] < intervals[i][0]:
                    new_array.append(newInterval)
                    merging = True
                new_array.append(intervals[i])
        if not merging:
            new_array.append(newInterval)
        return new_array
            