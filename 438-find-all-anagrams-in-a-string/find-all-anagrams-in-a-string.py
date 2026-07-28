class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if (len(p) > len(s)): 
            return ans
        
        count_p = dict()
        count_let = dict()
        for i in range(0, len(p)):
            count_p[p[i]] = count_p.get(p[i], 0) + 1
            count_let[s[i]] = count_let.get(s[i], 0) + 1
        
        if count_p == count_let:
            ans.append(0)
        
        for i in range(len(p), len(s)):
            count_let[s[i - len(p)]] -= 1
            count_let[s[i]] = count_let.get(s[i], 0) + 1
            if (count_let[s[i - len(p)]] == 0):
                del count_let[s[i - len(p)]]
            if count_p == count_let:
                ans.append(i - len(p) + 1)
        return ans
            
