class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = dict()
        for char in s:
            count[char] = count.get(char, 0) + 1

        left_chars = []
        middle = ""
        for char in sorted(count.keys()):  
            half = count[char] // 2
            left_chars.append(char * half)
            if count[char] % 2 == 1:
                middle = char 
        left = "".join(left_chars)
        return left + middle + left[::-1]