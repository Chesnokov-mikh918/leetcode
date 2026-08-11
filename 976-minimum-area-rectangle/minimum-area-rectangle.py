class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        min_area = 10**10
        for i in points:
            points_set.add((i[0], i[1]))

        for first in range(len(points)):
            x1, y1 = points[first]
            for second in range(first + 1, len(points)):
                x2, y2 = points[second]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in points_set and (x2, y1) in points_set:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        min_area = min(min_area, area)
        return 0 if min_area == 10**10 else min_area