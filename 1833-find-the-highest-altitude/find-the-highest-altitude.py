class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        max_mean = current
        for i in range(len(gain)):
            current = current + gain[i]
            max_mean = max(max_mean, current)
        return max_mean