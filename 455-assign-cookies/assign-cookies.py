class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        first = 0
        second = 0
        count = 0
        while (second < len(s) and first < len(g)):
            if (s[second] >= g[first]):
                count += 1
                first += 1
            second += 1
        return count