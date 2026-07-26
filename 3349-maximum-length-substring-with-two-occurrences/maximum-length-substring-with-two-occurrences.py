class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        characters = dict()
        left = 0
        right = -1
        max_len = 0
        while (left < len(s)):
            while (right + 1 < len(s) and characters.get(s[right + 1], 0) < 2):
                characters[s[right + 1]] = characters.get(s[right + 1], 0) + 1
                right += 1
            max_len = max(max_len, right - left + 1)

            characters[s[left]] -= 1
            left += 1
        return max_len
