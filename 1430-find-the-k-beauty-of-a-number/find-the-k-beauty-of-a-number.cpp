class Solution {
public:
    int divisorSubstrings(int num, int k) {
        int count = 0;
        std::string s = std::to_string(num);
        std::string temp;
        for (int i = 0; i < k; i++) {
            temp += s[i];
        }
        if (num % std::stoi(temp) == 0) {
            count++;
        }
        for (int i = k; i < s.length(); i++) {
            temp.erase(temp.begin());
            temp += s[i];
            if (std::stoi(temp) == 0) {
                continue;
            }
            if (num % std::stoi(temp) == 0) {
                count++;
            }
        }
        return count;
    }
};