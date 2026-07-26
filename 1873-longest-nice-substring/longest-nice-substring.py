class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        all_unique = set(s)
        for index, element in enumerate(s):
            if (element.swapcase() not in all_unique):
                sub_str1 = self.longestNiceSubstring(s[:index])
                sub_str2 = self.longestNiceSubstring(s[index + 1:])
                return max(sub_str1, sub_str2, key=len)
        return s