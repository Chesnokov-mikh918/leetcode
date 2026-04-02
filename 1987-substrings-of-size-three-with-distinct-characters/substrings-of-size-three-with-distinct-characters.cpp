class Solution {
public:
    int countGoodSubstrings(string s) {
        int max_count = 0;
        if (s.length() < 3) {
            return 0;
        }
        char s0 = s[0];
        char s1 = s[1];
        char s2 = s[2];
        if ((s0 != s1) && (s1 != s2) && (s0 != s2)) {
            max_count += 1;
        }
        for (int i = 3; i < s.length(); i++) {
            s0 = s1;
            s1 = s2;
            s2 = s[i];
            if ((s0 != s1) && (s1 != s2) && (s0 != s2)) {
                max_count += 1;
            }
        }
        return max_count;
    }
};