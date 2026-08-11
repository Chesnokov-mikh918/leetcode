class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda val: val[1])
        last_pos = points[0][1]
        count = 1
        not_null_que = False
        for i in range(1, len(points)):
            if points[i][0] > last_pos:
                count += 1
                last_pos = points[i][1]
        return count

