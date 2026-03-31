class Solution {
public:
    int myAtoi(string s) {
        int count = 0, i = 0;
        std::unordered_map<char, int>unique_int = { {'0', 0}, {'1', 1}, {'2', 2}, {'3', 3} , {'4', 4} ,{'5', 5} ,{'6', 6} ,{'7', 7} ,{'8', 8}, {'9', 9} };
        bool flag_neg = false, flag_pos = false, nothing = true, full = false;
        while (s[i] == ' ') {
            count++;
            i++;
        }
        std::string s1;
        s1 = s.substr(count, s.length() - count);
        
        
        if (s1[0] == '-') {
            flag_neg = true;
            flag_pos = false;
            nothing = false;
        }
        if (s1[0] == '+') {
            flag_pos = true;
            flag_neg = false;
            nothing = false;
        }
    
        std::string s2;
        if (flag_neg || flag_pos) {
            for (int i = 1; i < s1.size(); i++) {
                if (unique_int.count(s1[i])) {
                    s2 += s1[i];
                    continue;
                }
                break;
            }
        }
        else {
            for (int i = 0; i < s1.size(); i++) {
                if (unique_int.count(s1[i])) {
                    s2 += s1[i];
                    continue;
                }
                break;;
            }
        }
    
        long long ans = 0;
        int j = 0, count2 = 0;
        while (s2[j] == '0') {
            count2++;
            j++;
        }
    
        std::string s3;
        s3 = s2.substr(count2, s2.length() - count2);
        
        int len_str = s3.size();
        if (len_str > 10 && flag_neg) {
            ans = -pow(2, 31);
            full = true;
        }
        else if ((len_str > 10 && !flag_neg) || (len_str > 10 && nothing)) {
            ans = pow(2, 31) - 1;
            full = true;
        }
        else if (s3  == "2147483647" && flag_neg) {
            ans = -(pow(2, 31) - 1);
            full = true;
        }
        else if (s3  == "2147483647" && !flag_neg) {
            ans = pow(2, 31) - 1;
            full = true;
        }
        else {
            for (int i = 0; i < len_str;i++) {
                ans += unique_int[s3[i]] * pow(10, len_str - i - 1);
                if (ans > pow(2, 31) - 1 && flag_neg) {
                    ans = -pow(2, 31);
                    full = true;
                    break;
                }
                if ((ans > pow(2, 31) - 1 && !flag_neg) || (ans > pow(2, 31) - 1 && nothing)) {
                    ans = pow(2, 31) - 1;
                    full = true;
                    break;
                }
            }
        }

        if (flag_neg && ans != pow(2, 31) - 1 && ans != -pow(2, 31) && !full) {
            ans *= (-1);
        }
        return ans;
    }
};