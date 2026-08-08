class Solution:
    def is_overlapping(self, arr1: List[int], arr2: List[int]) -> bool:
        return max(arr1[0], arr2[0]) <= min(arr1[1], arr2[1])

    def merge_two(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return [min(arr1[0], arr2[0]), max(arr1[1], arr2[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda val: (val[0], val[1]))
        array = [intervals[0]]
        for i in range(1, len(intervals)):
            if (self.is_overlapping(array[-1], intervals[i])):
                array[-1] = self.merge_two(array[-1], intervals[i])
            else:
                array.append(intervals[i])
        return array