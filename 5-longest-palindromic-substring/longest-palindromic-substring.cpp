class Solution {
public:
    string longestPalindrome(string s) {
        std::string longest_palind; 
        longest_palind += s[0];
        for (int i = 1; i < s.length(); i++) {
            // first way of check
            std::string temp;
            temp += s[i];
            int left = i - 1;
            int right = i + 1;
            while (left >= 0 && right <= (s.length() - 1)) {
                if (s[left] == s[right]) {
                    temp = s[left] + temp + s[right];
                    left--;
                    right++;
                }
                else {
                    break;
                }
            }
            if (temp.length() > longest_palind.length()) {
                longest_palind = temp;
            }
            // second way of check
            std::string temp2;
            if (s[i] != s[i - 1]) {
                temp2 += s[i];
            }
            else {
                temp2 += s[i];
                temp2 += s[i - 1];
                int left = i - 2;
                int right = i + 1;
                while (left >= 0 && right <= s.length() - 1) {
                    if (s[left] == s[right]) {
                        temp2 = s[left] + temp2 + s[right];
                        left--;
                        right++;
                    }
                    else {
                        break;
                    }
                }
            }
            if (temp2.length() > longest_palind.length()) {
                longest_palind = temp2;
            }
        }
        return longest_palind;
    }
};