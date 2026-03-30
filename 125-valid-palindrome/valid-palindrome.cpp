class Solution {
public:
    bool isPalindrome(string s) {
        std::string new_str;
        for (int i = 0; i < s.length(); i++) {
            if ((int(s[i]) >= 48 && int(s[i]) <= 57) || (int(s[i]) >= 97 && int(s[i]) <= 122) || (int(s[i]) >= 65 && int(s[i]) <= 90)) {
                new_str += std::tolower(s[i]);
            }
        }
        
        int left = 0;
        int right = new_str.length() - 1;
        while (left <= right) {
            if (new_str[left] != new_str[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};