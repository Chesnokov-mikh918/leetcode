class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        right = len(s) - 1
        left = 0
        s = list(s)
        while(left < right):
            if ((s[left] in vowels) and (s[right] in vowels)):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif ((s[left] in vowels) and  not (s[right] in vowels)):
                right -= 1
            elif (not(s[left] in vowels) and (s[right] in vowels)):
                left += 1
            else:
                right -= 1
                left += 1
        return "".join(s)    
            