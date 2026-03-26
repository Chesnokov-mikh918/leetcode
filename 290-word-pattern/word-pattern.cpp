class Solution {
public:
    bool wordPattern(string pattern, string s) {
        std::string temp;
        std::unordered_map <char, std::string>ans;
        std::vector<std::string>data;
        std::unordered_set<char>pattern_symb;
        std::unordered_set<std::string>s_symb;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != ' ') {
                temp += s[i];
            }
            else {
                data.push_back(temp);
                temp = "";
            }
        }
        data.push_back(temp);

        if (pattern.length() != data.size()) {
            return false;
        }

        for (int i = 0; i < pattern.length(); i++) {
            pattern_symb.insert(pattern[i]);
            if (ans.count(pattern[i]) != 0) {
                if (ans[pattern[i]] != data[i]) {
                    return false;
                }
                continue;
            }
            else {
                ans[pattern[i]] = data[i];
                s_symb.insert(data[i]);
            }
        }
        if (s_symb.size() != pattern_symb.size()) {
            return false;
        }
        return true;
    }
};