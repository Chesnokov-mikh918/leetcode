class Solution:
    def reverse_word(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        while (left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)

    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        reversed_str = ""
        for i in range(0, len(s) - 1):
            reversed_str += (self.reverse_word(s[i]) + " ")
        reversed_str += self.reverse_word(s[-1])
        return reversed_str