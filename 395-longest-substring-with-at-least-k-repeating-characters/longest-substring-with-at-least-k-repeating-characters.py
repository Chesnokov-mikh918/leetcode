class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def recursion(s: str) -> int:
            if (len(s) == 0):
                return 0

            count_freq = dict()
            for i in range(0, len(s)):
                count_freq[s[i]] = count_freq.get(s[i], 0) + 1
            
            for keys, values in count_freq.items():
                if values < k:
                    return max([recursion(part) for part in s.split(keys)])
            return len(s)
        return recursion(s)