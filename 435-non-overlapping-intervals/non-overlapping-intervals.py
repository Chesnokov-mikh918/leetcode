class Solution:
    def is_overlapping(self, n: List[int], m: List[int]) -> bool:
        return max(n[0], m[0]) < min(n[1], m[1])

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = []
        intervals.sort(key=lambda val: (val[1], val[0]))
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if not self.is_overlapping(result[-1], intervals[i]):
                result.append(intervals[i])
        return len(intervals) - len(result)
