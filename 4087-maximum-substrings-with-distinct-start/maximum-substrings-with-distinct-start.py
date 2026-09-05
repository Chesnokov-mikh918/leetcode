class Solution:
    def maxDistinct(self, s: str) -> int:
        elements = {}
        count = 0
        for i in range(len(s)):
            if s[i] in elements:
                continue
            count += 1
            elements[s[i]] = 1
        return count